from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import uuid4

from models import Task, TaskInDB
from auth import get_current_user, admin_only

router = APIRouter()

# In-memory task store
tasks_db: List[TaskInDB] = []


# ---------------- CREATE TASK ----------------
@router.post("/tasks", response_model=TaskInDB)
def create_task(task: Task, user=Depends(get_current_user)):
    new_task = TaskInDB(
        id=str(uuid4()),
        owner=user["sub"],
        **task.dict()
    )
    tasks_db.append(new_task)
    return new_task


# ---------------- GET MY TASKS ----------------
@router.get("/tasks", response_model=List[TaskInDB])
def get_my_tasks(user=Depends(get_current_user)):
    return [task for task in tasks_db if task.owner == user["sub"]]


# ---------------- ADMIN: GET ALL TASKS ----------------
@router.get("/admin/tasks", response_model=List[TaskInDB])
def get_all_tasks(user=Depends(admin_only)):
    return tasks_db


# ---------------- UPDATE TASK ----------------
@router.put("/tasks/{task_id}", response_model=TaskInDB)
def update_task(task_id: str, updated_task: Task, user=Depends(get_current_user)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            if task.owner != user["sub"] and user["role"] != "admin":
                raise HTTPException(status_code=403, detail="Not allowed")

            updated = TaskInDB(
                id=task_id,
                owner=task.owner,
                **updated_task.dict()
            )
            tasks_db[index] = updated
            return updated

    raise HTTPException(status_code=404, detail="Task not found")


# ---------------- DELETE TASK ----------------
@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, user=Depends(get_current_user)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            if task.owner != user["sub"] and user["role"] != "admin":
                raise HTTPException(status_code=403, detail="Not allowed")

            tasks_db.pop(index)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
