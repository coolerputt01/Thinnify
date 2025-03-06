from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import date
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tododb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)
migrate = Migrate(app, database)

# Todo Model
class Todo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    task = database.Column(database.String(200), nullable=False)
    completed = database.Column(database.Boolean, default=False)
    category = database.Column(database.String(200), nullable=True,default='Others')
    timestamp = database.Column(database.Date, default=date.today())
    print(timestamp)

# Custom 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/api/todos', methods=['GET'], strict_slashes=False)
def get_todos():
    query = str(request.args.get('search', '')).lower()
    todos = Todo.query.all()
    print(query)
    if query:
        todos = [todo for todo in todos if query in todo.task.lower()]
    
    if not todos:  # Check if the filtered list is empty
        return jsonify({"error": "No Tasks Found"}), 404
    
    return jsonify([
        {"id": todo.id, "task": todo.task, "completed": todo.completed, "category": todo.category, "timestamp": todo.timestamp}
        for todo in todos
    ]), 200

# Get a Single Todo by ID
@app.route('/api/todo/<int:id>', methods=['GET'])
def get_individual_todo(id):
    todo = database.session.get(Todo, id)
    if not todo:
        return jsonify({"error": "Invalid ID. The todo might not exist."}), 404

    return jsonify({
        "id": todo.id,
        "task": todo.task,
        "completed": todo.completed,
        "category": todo.category
    })

# Create a New Todo
@app.route('/api/todo', methods=['POST'])
def create_todo():
    data = request.get_json()

    if not data or 'task' not in data or 'category' not in data:
        return jsonify({"error": "Task and category are required fields"}), 400

    new_todo = Todo(
        task=data['task'],
        category=data['category'],
        completed=data.get('completed', False)  # Default to False if not provided
    )

    database.session.add(new_todo)
    database.session.commit()

    return jsonify({"message": "Todo created successfully!", "todo": {
        "id": new_todo.id,
        "task": new_todo.task,
        "completed": new_todo.completed,
        "category": new_todo.category,
        "timestamp": new_todo.timestamp
    }}), 201

# Update a Todo
@app.route('/api/todo/<int:id>', methods=['PUT'])
def update_task(id):
    todo = database.session.get(Todo, id)
    if not todo:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Update attributes if provided
    if 'task' in data:
        todo.task = data['task']
    if 'completed' in data:
        todo.completed = data['completed']
    if 'category' in data:
        todo.category = data['category']
    
    database.session.commit()
    
    return jsonify({
        "message": "Task updated successfully!",
        "task": {
            "id": todo.id,
            "task": todo.task,
            "completed": todo.completed,
            "category": todo.category,
            "timestamp": todo.timestamp
        }
    })

# Delete a Todo
@app.route('/api/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = database.session.get(Todo, id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    database.session.delete(todo)
    database.session.commit()
    
    return jsonify({"message": "Todo deleted successfully!"}), 200

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    app.run(debug=True)