from fastapi import FastAPI, Path, Query # No me deja importar HTTPExceptions 
from pydantic import BaseModel
from typing import Annotated, Optional
#from starlette.exceptions import HTTPExceptions

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

class UpdateItem(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


inventory = {}

# Como crear un inventario y actualizarlo??
# Se pueden definir varias funciones en cada endpoint??
# Repasar los status codes
# async necesario?
# Annotated vs Optional vs | None = None

# Run the API: uvicorn eduAPI:app --reload

@app.get("/item/{item_id}")
async def get_item(item_id : int = Path(..., description = "The ID of the item you'd like to view.")):
    if item_id not in inventory:
        raise HTTPExceptions(status_code = 404, detail = "Item ID not found.")
    return inventory[item_id]

@app.get("/item/get-by-name") # Probando pasar el nombre como paramtro Query
async def get_item(name : str = Query(..., title = "Name", description = "Name of the item.")):
    for item in inventory:
        if inventory[item].name == name:
            return inventory[item]
    raise HTTPExceptions(status_code = 404, detail = "Item name not found.")

@app.post("/create-item/{item_id}")
async def create_item(item_id : int, item : Item):
    if item_id in inventory:
        raise HTTPExceptions(status_code = 400, detail = "Item ID already exists.")
    
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
async def update_item(item_id : int, item : UpdateItem):
    if item_id not in inventory:
        raise HTTPExceptions(status_code = 404, detail = "Item ID does not exists.")
    
    if item.name != None:
        inventory[item_id].name = item.name

    if item.description != None:
        inventory[item_id].description = item.description
    
    if item.price != None:
        inventory[item_id].price = item.price

    return inventory[item_id]

@app.delete("/delete-item") # Probando pasar item_id como parametro Query
async def delete_item(item_id : int = Query(..., description = "The ID of th item to delete.")):
    if item_id not in inventory:
        raise HTTPExceptions(status_code = 404, detail = "Item ID does not exists.")
    
    del inventory[item_id]
    return {"Success" : "Item deleted"}