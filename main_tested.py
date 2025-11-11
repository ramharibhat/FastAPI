from typing import Union
from fastapi import FastAPI
from enum import Enum 

from pydantic import BaseModel

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet  = "resnet"
    lenet  =  "lenet"

class Item(BaseModel):
    name: str
    price: float
    is_offer : Union [bool, None] = None

fake_db_data = [{"item_name": "foo"}, {"item_name": "bar"}, {"item_name" : "tax"}]

@app.get("/items/")
async def read_items(skip : int = 0, limit : int =10):
    return fake_db_data[skip: skip + limit]

@app.get("/files/{file_path: path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Model is alexnet "}
    
    if model_name.value == "lenet" :
        return {"model_name": model_name, "message": "Model is lenet "}
    return {"model_name": model_name, "message": "Model is resnet"}


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]= None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_items(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}