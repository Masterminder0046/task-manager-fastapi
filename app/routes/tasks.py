from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/tasks")

# CREATE TASK
@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# GET ALL TASKS (with optional filter)
@router.get("/")
def get_tasks(completed: bool = None, db: Session = Depends(get_db), user=Depends(get_current_user)):
    query = db.query(Task).filter(Task.user_id == user.id)

    if completed is not None:
        query = query.filter(Task.completed == completed)

    return query.all()


# GET SINGLE TASK
@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# UPDATE TASK
@router.put("/{task_id}")
def update_task(task_id: int, updated: TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if updated.title is not None:
        task.title = updated.title
    if updated.description is not None:
        task.description = updated.description
    if updated.completed is not None:
        task.completed = updated.completed

    db.commit()
    db.refresh(task)

    return task


# DELETE TASK
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}
