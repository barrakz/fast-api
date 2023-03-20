from fastapi import FastAPI, Path

app = FastAPI()


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
