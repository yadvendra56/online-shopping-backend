from fastapi import APIRouter

router = APIRouter()

@router.post("/add")
def add_to_cart(item: dict):
    return {"message": "Item added to cart", "item": item}

@router.get("/{user_id}")
def get_cart(user_id: int):
    return {"user_id": user_id, "cart": []}
