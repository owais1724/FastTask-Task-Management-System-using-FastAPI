from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# -----------------------------
# Data Models
# -----------------------------
class Task(BaseModel):
    title: str
    description: str
    completed: bool = False


class TaskInDB(Task):
    id: str


# -----------------------------
# In-memory database
# -----------------------------
tasks_db: List[TaskInDB] = []


# -----------------------------
# CREATE
# -----------------------------
@app.post("/tasks", response_model=TaskInDB)
def create_task(task: Task):
    new_task = TaskInDB(
        id=str(uuid4()),
        **task.dict()
    )
    tasks_db.append(new_task)
    return new_task


# -----------------------------
# READ ALL
# -----------------------------
@app.get("/tasks", response_model=List[TaskInDB])
def get_all_tasks():
    return tasks_db


# -----------------------------
# READ ONE
# -----------------------------
@app.get("/tasks/{task_id}", response_model=TaskInDB)
def get_task(task_id: str):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# -----------------------------
# UPDATE
# -----------------------------
@app.put("/tasks/{task_id}", response_model=TaskInDB)
def update_task(task_id: str, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            updated = TaskInDB(
                id=task_id,
                **updated_task.dict()
            )
            tasks_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


# -----------------------------
# DELETE
# -----------------------------
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
