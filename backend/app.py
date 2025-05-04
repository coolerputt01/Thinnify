from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

# Initialize Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app, origins=["https://thinnify.surge.sh"])

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False, default='Others')
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    endate = db.Column(db.DateTime, nullable=True,default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'completed': self.completed,
            'user_id': self.user_id,
            'endate': self.endate,
            'created': self.created.isoformat() if self.created else None
        }

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has expired"}), 401

# Register Route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except:
        db.session.rollback()
        return jsonify({"message": "User might already exist or DB error occurred"}), 400


# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=str(user.id))
        print("Found")
        return jsonify({"access_token": access_token, "userId": user.id, "userName": user.username}), 200
    
    return jsonify({"message": "Invalid credentials!"}), 401

# Get Todos (Protected)
@app.route('/todos', methods=['GET'])
@jwt_required()
def get_todos():
    user_id = get_jwt_identity()
    todos = Todo.query.filter_by(user_id=user_id).all()
    return jsonify([todo.to_dict() for todo in todos]), 200

# Create Todo (Protected)
@app.route('/todo', methods=['POST'])
@jwt_required()
def create_todo():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_todo = Todo(title=data['title'], category=data['category'], endate=data.get('endate'), user_id=user_id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

# Update Todo (Protected)
@app.route('/todo/<int:todo_id>', methods=['PUT'])
@jwt_required()
def update_todo(todo_id):
    user_id = get_jwt_identity()
    todo = db.session.get(Todo, todo_id)
    if not todo or str(todo.user_id) != str(user_id):
        return jsonify({"message": "Unauthorized or not found!"}), 403
    data = request.get_json()
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify(todo.to_dict()), 200

# Delete Todo (Protected)
@app.route('/todo/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    user_id = get_jwt_identity()
    todo = Todo.query.get(todo_id)
    if not todo or todo.user_id != user_id:
        return jsonify({"message": "Unauthorized or not found!"}), 403
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted successfully!"}), 200


# Search Todos (Protected)
@app.route('/todos/search', methods=['GET'])
@jwt_required()
def search_todos():
    user_id = get_jwt_identity()
    query = request.args.get('q', '').strip().lower()

    if not query:
        return jsonify({"message": "Search query is required"}), 400

    # Simple case-insensitive search in title and category
    todos = Todo.query.filter(
        Todo.user_id == user_id,
        (Todo.title.ilike(f"%{query}%")) | (Todo.category.ilike(f"%{query}%"))
    ).all()

    return jsonify([todo.to_dict() for todo in todos]), 200

# Run Flask App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
