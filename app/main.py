from services.task_service import TaskService
from models.task import Task
from datetime import date
from fastapi import FastAPI


app = FastAPI()

tasks = [
    Task(
        title="Cooking",
        priority="Medium",
        due_date=date(2026, 10, 3),
        status="Not Started"
    ),
    Task(
        title="Complete project report",
        priority="High",
        description="Finalize and submit the project report by the end of the week.",
        due_date=date(2024, 6, 15),
        status="Completed"
    ),
    Task(
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


# TaskService.get_daily_summary(tasks)
