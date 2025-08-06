from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: int
    task: str
    done: Optional[bool] = False
