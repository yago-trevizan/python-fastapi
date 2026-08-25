from models.task_model import Task
from models.user_model import User

tasks: list[Task] = [
  Task(id=1, title="Study Docker", done=True, user_id=1),
  Task(id=2, title="Learn FastAPI", done=False, user_id=1),
  Task(id=3, title="Practice SQLAlchemy", done=True, user_id=1),
  Task(id=4, title="Create a REST API", done=False, user_id=2),
  Task(id=5, title="Study PostgreSQL", done=False, user_id=1),
  Task(id=6, title="Review Python concepts", done=True, user_id=2),
  Task(id=7, title="Practice object-oriented programming", done=False, user_id=1),
  Task(id=8, title="Study databases", done=True, user_id=2),
  Task(id=9, title="Create a project with Docker", done=False, user_id=1),
  Task(id=10, title="Study JWT authentication", done=False, user_id=2),
  Task(id=11, title="Learn automated testing", done=False, user_id=1),
  Task(id=12, title="Practice Git and GitHub", done=True, user_id=1),
  Task(id=13, title="Study relationships in SQLAlchemy", done=False, user_id=1),
  Task(id=14, title="Create endpoints with PATCH and DELETE", done=True, user_id=1),
  Task(id=15, title="Document the project", done=False, user_id=2),
]

users: list[User] = [
  User(id=1, name="John Doe", username="john_d", password="$argon2id$v=19$m=65536,t=3,p=4$gqJ9VogPzcbiAbzc7/t3uw$0cGc9HM/hCcEpyl5DxFwhs+v0uAoxmGdY2eANYrDRCM"),
  User(id=2, name="Foo Bar", username="foo_b", password="$argon2id$v=19$m=65536,t=3,p=4$gqJ9VogPzcbiAbzc7/t3uw$0cGc9HM/hCcEpyl5DxFwhs+v0uAoxmGdY2eANYrDRCM"),
]
