from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_cors import CORS
from flask_session import Session  # Added for session support
from datetime import datetime

app = Flask(__name__)

# Database and Secret Key Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'todo_secret'

# Session Config
app.config['SESSION_TYPE'] = 'filesystem'  # Store sessions in the file system
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_FILE_DIR'] = "./flask_session"

# Initialize Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
Session(app)  # Initialize session storage
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Enable CORS
CORS(
    app,
    origins=["http://localhost:8080"],
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)

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
    created = db.Column(db.DateTime, default=datetime.utcnow)
    endate = db.Column(db.String(120), nullable=True)

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

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

# Flask-Login User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"message": "Unauthorized access. Please log in."}), 401

# Register Route
@app.route('/check-session', methods=['GET'])
def check_session():
    if current_user.is_authenticated:
        return jsonify({"message": "User is logged in", "user": current_user.username}),200
    else:
        return jsonify({"message": "User is NOT logged in"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except:
        return jsonify({"message": "User already exists!"}), 400

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)  # Store user in session
        session['user_id'] = user.id  # Store user_id explicitly in session
        return jsonify({"message": "Logged in successfully!", "userId": user.id, "userName": user.username}), 200

    return jsonify({"message": "Invalid credentials!"}), 401

# Logout Route
@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    session.pop('user_id', None)  # Remove user from session
    return jsonify({"message": "Logged out successfully!"}), 200

# Get Todos (Protected)
@app.route('/todos', methods=['GET'])
@login_required
def get_todos():
    print(current_user)
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return jsonify([todo.to_dict() for todo in todos]), 200

# Search Todos (Protected)
@app.route('/todos/search', methods=['GET'])
@login_required
def search_todos():
    query = request.args.get('query')
    if query:
        todos = Todo.query.filter(Todo.title.like(f'%{query}%'), Todo.user_id == current_user.id).all()
        return jsonify([todo.to_dict() for todo in todos]), 200
    return jsonify({"message": "No search query provided."}), 400

# Create Todo (Protected)
@app.route('/todo', methods=['POST'])
@login_required
def create_todo():
    data = request.get_json()
    new_todo = Todo(title=data['title'], category=data['category'], endate=data['endate'], user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

# Update Todo (Protected)
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

# Delete Todo (Protected)
@app.route('/todo/<int:todo_id>', methods=['DELETE'])
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo or todo.user_id != current_user.id:
        return jsonify({"message": "Unauthorized or not found!"}), 403
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted successfully!"}), 200

# Run Flask App
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
