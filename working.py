from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Path

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand = Optional[str] = None


@app.get('/')
def home():
    return {'Data': 'Test'}


@app.get('/about')
def about():
    return {'About': 'Info about me'}


inventory = {
    1: {
        "name": "Milk",
        "price": 3.79,
        "brand": "Laciate"
    },
    2: {
        "name": "Water",
        "price": 2.99,
        "brand": "Muszynianka"
    }
}


@app.get('/get-product/{item_id}')
def get_product(item_id: int = Path(..., description="The ID of the Item", gt=0, lt=3)):
    return inventory[item_id]


@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data:": "Not found."}


@app.post("/create-item")
def create_item(item: Item):
    return {}
