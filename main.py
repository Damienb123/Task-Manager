from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello API World"}

# build task endpoints using CRUD
tasks = []
# create a task
@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return{"task": task}
# get a new task
@app.get("/tasks")
def get_task():
    return {"tasks": tasks}


class Task(BaseModel):
    title: str
    completed: bool = False

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

# update and delete tasks for completion of CRUD
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks.pop(task_id)
    return{"message": "Task deleted"}