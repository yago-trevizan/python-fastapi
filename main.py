from fastapi import FastAPI
from routes.tasks_router import task_router
from routes.auth_router import auth_router

app = FastAPI()

app.include_router(task_router)
app.include_router(auth_router)
