from typing import List, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []


class Item02(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: List[str] = []


class Item03(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


class Image(BaseModel):
    url: str
    name: str


class Image02(BaseModel):
    url: HttpUrl
    name: str


class Item04(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items04/{item_id}")
async def update_item04(item_id: int, item04: Item04):
    results = {"item_id": item_id, "item": item04}
    return results


class Item05(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


@app.put("/items05/{item_id}")
async def update_item(item_id: int, item05: Item05):
    results = {"item_id": item_id, "item": item05}
    return results


class Image06(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images06/multiple/")
async def create_multiple_images(images: List[Image06]):
    return images


@app.post("/index-weights01/")
async def create_index_weights(weights: Dict):
    return weights


@app.post("/index-weights02/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
