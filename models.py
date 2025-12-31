from pydantic import BaseModel
from typing import Optional

# -------- User --------
class User(BaseModel):
    username: str
    role: str


# -------- Task Input --------
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


# -------- Task Output --------
class TaskInDB(Task):
    id: str
    owner: str
