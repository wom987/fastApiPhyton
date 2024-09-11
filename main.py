from uuid import uuid4

from fastapi import FastAPI,Body
from typing import List
from models import User, Gender, Role

app = FastAPI()
db: List[User] = [
    User(id=uuid4(), first_name="John", last_name="Doe", middle_name="Roland", gender=Gender.male, roles=[Role.user]),
    User(id=uuid4(), first_name="Carlos", last_name="Sanatana", middle_name="D", gender=Gender.male, roles=[Role.admin]),
    User(id=uuid4(), first_name="Keren", last_name="Morales", middle_name="S", gender=Gender.female, roles=[Role.student, Role.user]),
]

@app.get("/")
async def root():
    return {"message": "Hello Worldcsssss"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/api/v1/users")
async def fetch_users():
    return db
@app.post("/api/v1/users")
async def create_user(user: User = Body(...)):
    db.append(user)
    return {"user": user}
