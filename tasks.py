from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import uuid4

from models import Task, TaskInDB
from auth import get_current_user, admin_only

router = APIRouter()

# In-memory database
tasks_db: List[TaskInDB] = []


# -------------------------------------------------
# CREATE TASK (Admin & Customer)
# -------------------------------------------------
@router.post("/tasks", response_model=TaskInDB)
def create_task(task: Task, user=Depends(get_current_user)):
    new_task = TaskInDB(
        id=str(uuid4()),
        owner=user["sub"],
        **task.dict()
    )
    tasks_db.append(new_task)
    return new_task


# -------------------------------------------------
# GET MY TASKS (Customer & Admin)
# -------------------------------------------------
@router.get("/tasks", response_model=List[TaskInDB])
def get_my_tasks(user=Depends(get_current_user)):
    return [task for task in tasks_db if task.owner == user["sub"]]


# -------------------------------------------------
# GET TASK BY ID (Owner or Admin)
# -------------------------------------------------
@router.get("/tasks/{task_id}", response_model=TaskInDB)
def get_task_by_id(task_id: str, user=Depends(get_current_user)):
    for task in tasks_db:
        if task.id == task_id:
            if task.owner != user["sub"] and user["role"] != "admin":
                raise HTTPException(status_code=403, detail="Not allowed")
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# -------------------------------------------------
# ADMIN: GET ALL TASKS
# -------------------------------------------------
@router.get("/admin/tasks", response_model=List[TaskInDB])
def get_all_tasks(user=Depends(admin_only)):
    return tasks_db


# -------------------------------------------------
# UPDATE TASK (Owner or Admin)
# -------------------------------------------------
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


# -------------------------------------------------
# DELETE TASK (ADMIN ONLY)
# -------------------------------------------------
@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, user=Depends(admin_only)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": "Task deleted by admin"}

    raise HTTPException(status_code=404, detail="Task not found")
