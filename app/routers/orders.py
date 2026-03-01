from fastapi import APIRouter

router = APIRouter()

@router.post("/place")
def place_order(order: dict):
    return {"message": "Order placed successfully", "order": order}

@router.get("/{order_id}")
def get_order(order_id: int):
    return {"order_id": order_id, "status": "Processing"}
