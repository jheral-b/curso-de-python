from fastapi import FastAPI

from routers import products, users

# Documentación: https://fastapi.tiangolo.com/es/

# Para instalar FastAPI --> pip install "fastapi[all]"

# Con el plugin de "Thunder Client" para vscode, realize las peticiones http

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

# Url local: http://127.0.0.1:8000
@app.get("/") 
async def root():
    return "Hola FastAPI"

# Url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {"url_curso":"https://www.google.com"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
