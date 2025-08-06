from fastapi import FastAPI
from controllers import todo_controller

app = FastAPI()

app.include_router(todo_controller.router)
