from fastapi import APIRouter

router = APIRouter(
    prefix="/products", 
    responses={404: {"message": "No encontrado"}},
    tags=["products"]
)

products_list = ["product 1", "product 2", "product 3", "product 4", "product 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]