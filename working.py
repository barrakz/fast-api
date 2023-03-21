from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Path, Query

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


@app.get('/')
def home():
    return {'Data': 'Test'}


@app.get('/about')
def about():
    return {'About': 'Info about me'}


inventory = {}


@app.get('/get-product/{item_id}')
def get_product(item_id: int = Path(..., description="The ID of the Item", gt=0)):
    return inventory[item_id]


@app.get("/get-by-name/")
def get_item(name: str = Query(None, title="Name", description="Name of item.", max_length=10, min_length=2)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data:": "Not found."}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID exist"}

    inventory[item_id] = item
    return inventory[item_id]
