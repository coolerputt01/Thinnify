from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'todo'

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
CORS(app)

# User Model
class User(UserMixin, db.Model):
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
    user = db.relationship('User', backref=db.backref('todos', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'completed': self.completed,
            'user_id': self.user_id
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except Exception:
        return jsonify({"message": "User already exists!"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Logged in successfully!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!"}), 200

@app.route('/todos', methods=['GET'])
@login_required
def get_todos():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return jsonify([todo.to_dict() for todo in todos]), 200

@app.route('/todos/search', methods=['GET'])
@login_required
def search_todos():
    query = request.args.get('query')
    if query:
        todos = Todo.query.filter(Todo.title.like(f'%{query}%'), Todo.user_id == current_user.id).all()
        return jsonify([todo.to_dict() for todo in todos]), 200
    return jsonify({"message": "No search query provided."}), 400

@app.route('/todo', methods=['POST'])
@login_required
def create_todo():
    data = request.get_json()
    new_todo = Todo(title=data['title'], category=data['category'], user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

@app.route('/todo/<int:todo_id>', methods=['PUT'])
@login_required
def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo or todo.user_id != current_user.id:
        return jsonify({"message": "Unauthorized or not found!"}), 403
    data = request.get_json()
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify(todo.to_dict()), 200

@app.route('/todo/<int:todo_id>', methods=['DELETE'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo or todo.user_id != current_user.id:
        return jsonify({"message": "Unauthorized or not found!"}), 403
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted successfully!"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)