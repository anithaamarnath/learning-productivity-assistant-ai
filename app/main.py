from services.task_service import TaskService
from models.task import Task
from datetime import date
from fastapi import FastAPI


app = FastAPI()

tasks = [
    Task(
        id=1,
        title="Cooking",
        priority="Medium",
        due_date=date(2026, 10, 5),
        status="Not Started"
    ),
    Task(
        id=2,
        title="Complete project report",
        priority="High",
        description="Finalize and submit the project report by the end of the week.",
        due_date=date(2024, 6, 15),
        status="Completed"
    ),
    Task(
        id=3,
        title="Apply for job",
        priority="High",
        description="Submit job applications to potential employers.",
        due_date=date(2026, 10, 2),
        status="In Progress"
    )
]


@app.get("/")
def home():
    return {"message": "Welcome to the Task Management API!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    return {"message": "Task not found"}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    return {"message": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(index)
            return {"message": "Task deleted successfully", "task": deleted_task}
    return {"message": "Task not found"}


@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.get("/tasks/today")
def get_today_task():
    return TaskService.get_today_tasks(tasks)


@app.get("/tasks/overdue")
def get_overdue_tasks():
    return TaskService.get_overdue_tasks(tasks)


@app.get("/tasks/completed")
def get_completed_tasks():
    return TaskService.get_completed_tasks(tasks)


@app.get("/tasks/summary")
def get_daily_summary():
    return TaskService.get_daily_summary(tasks)


# TaskService.get_daily_summary(tasks)
