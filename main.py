from fastapi import FastAPI
from routes.tasks_router import task_router

app = FastAPI()

app.include_router(task_router)
