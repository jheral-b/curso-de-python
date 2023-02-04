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

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user

@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user

@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
        
    if not found:
        return {"error": "Usuario no eliminado"}



# Funcion que realiza el filtro por "id"
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)

    try:
        return list(users)[0]

    except:
        return {"error":"User not found :("} 
        