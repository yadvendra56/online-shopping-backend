from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user(user: dict):
    return {"message": "User registered successfully", "user": user}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Sample User"}
