from fastapi import FastAPI
from app.routers import products

app = FastAPI(title="Online Shopping API")

app.include_router(products.router, prefix="/products", tags=["Products"])

@app.get("/")
def root():
    return {"message": "Online Shopping Backend Running"}
