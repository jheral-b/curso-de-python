from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str


users_db = {
    "Jheral": {
        "username": "JheralBR",
        "full_name": "Jheral Andres Barrera Riquelme",
        "email": "jheral.andres@gmail.com",
        "disabled": False,
        "password": "123456"
    },

    "Pequita": {
        "username": "Elmockito",
        "full_name": "Carolina Fernanda Concha Cortes",
        "email": "carolina.fernanda@gmail.com",
        "disabled": True,
        "password": "654321"
    },
}

def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    form.username
