from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 50000},
        {"id": 2, "name": "Phone", "price": 20000}
    ]
