import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud, schemas, database

router = APIRouter()
logger = logging.getLogger("app")

@router.post("/tasks/", response_model=schemas.Task)
def create_new_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_task(db=db, task=task)
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=400, detail=f"Error creating task: {e}")

@router.get("/tasks/", response_model=List[schemas.Task])
def read_all_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    try:
        tasks = crud.get_tasks(db, skip=skip, limit=limit)
        return tasks
    except Exception as e:
        logger.error(f"Error retrieving tasks: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving tasks: {e}")

@router.get("/tasks/{task_id}", response_model=schemas.Task)
def read_single_task(task_id: int, db: Session = Depends(database.get_db)):
    try:
        db_task = crud.get_task(db, task_id=task_id)
        if db_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return db_task
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error retrieving task: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving task: {e}")

@router.put("/tasks/{task_id}", response_model=schemas.Task)
def update_single_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(database.get_db)):
    try:
        db_task = crud.update_task(db, task_id=task_id, task=task)
        if db_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return db_task
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error updating task: {e}")
        raise HTTPException(status_code=400, detail=f"Error updating task: {e}")

@router.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_single_task(task_id: int, db: Session = Depends(database.get_db)):
    try:
        db_task = crud.delete_task(db, task_id=task_id)
        if db_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return db_task
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logger.error(f"Error deleting task: {e}")
        raise HTTPException(status_code=400, detail=f"Error deleting task: {e}")