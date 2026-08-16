from fastapi import FastAPI, Depends
from routes.tasks_router import task_router
from routes.auth_router import auth_router

def fake_dependency():
  return None

app = FastAPI(dependencies=[Depends(fake_dependency)])

app.include_router(task_router)
app.include_router(auth_router)
