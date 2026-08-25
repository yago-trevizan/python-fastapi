from models.task_model import Task
from models.user_model import User

tasks: list[Task] = [
  Task(id=1, title="Estudar Docker", done=True, user_id=1),
  Task(id=2, title="Aprender FastAPI", done=False, user_id=1),
  Task(id=3, title="Praticar SQLAlchemy", done=True, user_id=1),
  Task(id=4, title="Criar uma API REST", done=False, user_id=2),
  Task(id=5, title="Estudar PostgreSQL", done=False, user_id=1),
  Task(id=6, title="Revisar conceitos de Python", done=True, user_id=2),
  Task(id=7, title="Praticar programação orientada a objetos", done=False, user_id=1),
  Task(id=8, title="Estudar bancos de dados", done=True, user_id=2),
  Task(id=9, title="Criar um projeto com Docker", done=False, user_id=1),
  Task(id=10, title="Estudar autenticação com JWT", done=False, user_id=2),
  Task(id=11, title="Aprender testes automatizados", done=False, user_id=1),
  Task(id=12, title="Praticar Git e GitHub", done=True, user_id=1),
  Task(id=13, title="Estudar relacionamentos no SQLAlchemy", done=False, user_id=1),
  Task(id=14, title="Criar endpoints com PATCH e DELETE", done=True, user_id=1),
  Task(id=15, title="Documentar o projeto", done=False, user_id=2),
]

usuarios: list[User] = [
  User(id=1, name="John Doe", username="john_d", password="$argon2id$v=19$m=65536,t=3,p=4$gqJ9VogPzcbiAbzc7/t3uw$0cGc9HM/hCcEpyl5DxFwhs+v0uAoxmGdY2eANYrDRCM"),
  User(id=2, name="Foo Bar", username="foo_b", password="$argon2id$v=19$m=65536,t=3,p=4$gqJ9VogPzcbiAbzc7/t3uw$0cGc9HM/hCcEpyl5DxFwhs+v0uAoxmGdY2eANYrDRCM"),
]
