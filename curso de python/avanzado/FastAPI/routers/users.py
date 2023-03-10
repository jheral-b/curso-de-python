from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    responses={404: {"message": "No encontrado"}},
    tags=["users"]
)

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

# @router.get("/usersjson")
# async def usersjson():
#     return [
#         {
#             "name": "Jheral",
#             "surname": "Barrera",
#             "age": "22"
#         },
#         {
#             "name": "Andres",
#             "surname": "Riquelme",
#             "age": "18"
#         },
#         {
#             "name": "Pequita",
#             "surname": "Concha",
#             "age": "21"
#         }
#     ]

# Se muestra la lista de usuarios completa
@router.get("/")
async def users():
    return users_list

# Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

# Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)

@router.post("/", status_code=201, response_model= User)
async def user(user: User):
    
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=409, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return user

@router.put("/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user

@router.delete("/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

        return {"error": "No se ingreso el usuario"}
    else:
        
        users_list.append(user)
    return user

# Funcion que realiza el filtro por "id"
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)

    try:
        return list(users)[0]

    except:
        return {"error":"User not found :("} 