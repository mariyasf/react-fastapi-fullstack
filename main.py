from fastapi import FastAPI
from typing import Optional
from data.product import product_list
from enum import Enum
from fastapi.middleware.cors import CORSMiddleware

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


# -------------------------
# STATIC ROUTES (Fixed URL)
# -------------------------

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI server"}

@app.get("/about")
def about():
    return {"message": "This is About page"}

@app.get("/contact")
def contact():
    return {"message": "This is Contact page"}

  
# PRODUCTS ROUTE (QUERY PARAM)
# -------------------------
@app.get("/products/all")
def products(order: Optional[str] = None):
    if order == "desc":
        sorted_products = sorted(product_list, key=lambda x: x["id"], reverse=True)
    else:
        sorted_products = sorted(product_list, key=lambda x: x["id"])

    return {
        "order": order,
        "products": sorted_products
    }

@app.get("/products/sorted")
def products_sorted(order: SortOrder = SortOrder.asc):
    if order == SortOrder.desc:
        sorted_products = sorted(product_list, key=lambda x: x["id"], reverse=True)
    else:
        sorted_products = sorted(product_list, key=lambda x: x["id"])

    return {
        "order": order,
        "products": sorted_products
    }


# -------------------------
#  DYNAMIC ROUTES (Variable URL)
# -------------------------

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": "User details fetched"
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "message": "Product details fetched"
    }