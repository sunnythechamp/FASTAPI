from fastapi import APIRouter
from models.todo_model import Todo
from services import todo_service

router = APIRouter()

@router.get("/todos")
def get_todos():
    return todo_service.get_all_todos()

@router.post("/todos")
def create_todo(todo: Todo):
    return todo_service.add_todo(todo)

@router.delete("/todos/{todo_id}")
def remove_todo(todo_id: int):
    return todo_service.delete_todo(todo_id)
