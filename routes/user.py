from msilib import gen_uuid

from fastapi import APIRouter
from pydantic.types import UUID4

from config.db import conect
from models.user import users
from schemas.users import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/users")
def get_users():
    print(gen_uuid())
    return conect.execute(users.select()).fetchall()


@user.post("/createUser")
def create_user(userdb: User):
    new_user = {"username": userdb.username, "first_name": userdb.first_name, "last_name": userdb.last_name, "dni": userdb.dni,
                "phone": userdb.phone, "email": userdb.email, "password": f.encrypt(userdb.password.encode("utf-8")),
                "role": userdb.role}
    result = conect.execute(users.insert().values(new_user))
    print(result)
    print(new_user)
    return "create"


@user.get("/editUser")
def login():
    return "actualizar"


@user.get("/deleteUsers")
def login():
    return "eliminar"
