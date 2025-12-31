from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


class TaskInDB(Task):
    id: str
    owner: str
