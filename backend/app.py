from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tododb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)

# Todo Model
class Todo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    task = database.Column(database.String(200), nullable=False)
    completed = database.Column(database.Boolean, default=False)
    category = database.Column(database.String(200), nullable=False)

with app.app_context():
    database.create_all()

# Custom 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Get All Todos
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = database.session.query(Todo).all()
    if not todos:
        return jsonify({"error": "No todos found. You need to create some first!"}), 404

    return jsonify([
        {"id": todo.id, "task": todo.task, "completed": todo.completed, "category": todo.category}
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
    data = request.json

    if 'task' not in data or 'category' not in data:
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
        "category": new_todo.category
    }}), 201

# Update a Todo
@app.route('/api/todo/<int:id>', methods=['PUT'])
def update_task(id):
    todo = database.session.get(Todo, id)
    if not todo:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    
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
            "category": todo.category
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
    app.run(debug=True)
