from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Creamos la clase el cual tendra la estructura predefinida
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    birthdate: str

# Creamos una lista en la cual se alojan las clases creadas de los usuarios
users_list = [
    User(id=1, name="Jheral", surname="Barrera", age=22,  birthdate="16/08/00"),
    User(id=2, name="Andres", surname="Riquelme", age=18, birthdate="16/08/00"),
    User(id=3, name="Pequita", surname="Concha", age=21, birthdate="03/11/01")
]

@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Jheral",
            "surname": "Barrera",
            "age": "22"
        },
        {
            "name": "Andres",
            "surname": "Riquelme",
            "age": "18"
        },
        {
            "name": "Pequita",
            "surname": "Concha",
            "age": "21"
        }
    ]

# Se muestra la lista de usuarios completa
@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)

# Funcion que realiza el filtro por "id"
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)

    try:
        return list(users)[0]

    except:
        return {"error":"User not found :("} 