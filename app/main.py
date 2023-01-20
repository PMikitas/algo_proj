from typing import Union

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}



class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: str

# @app.post("/items/")
# async def create_item(item: Item):
#     return item
from typing import List

from fastapi import FastAPI, Query

app = FastAPI()
@app.get("/items/")
def read_items(q: List[str] = Query(None)):
    from joblib import dump, load
    import numpy as np
    clf999 = load('/code/app/model.joblib')
    return bool(clf999.predict(np.array(q).reshape(1,-1)))