from fastapi import FastAPI
from routes.tasks_router import task_router
from routes.auth_router import auth_router
from routes.users_router import user_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(user_router)
