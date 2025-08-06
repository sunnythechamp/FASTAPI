from models.todo_model import Todo

# In-memory storage
todos = []

def get_all_todos():
    return todos

def add_todo(todo: Todo):
    todos.append(todo)
    return todo

def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return {"message": f"Todo with ID {todo_id} deleted"}
