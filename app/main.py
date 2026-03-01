from fastapi import FastAPI
from app.routers import products, users, cart, orders

app = FastAPI(title="Online Shopping API")

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "Online Shopping Backend Running"}
