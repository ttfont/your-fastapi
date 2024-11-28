from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items01/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items02/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user01/")
async def create_user(user: UserIn) -> UserIn:
    return user


@app.post("/user02/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


class Item01(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items01 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item01, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items01[item_id]


class Item02(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items02 = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item02,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items02[item_id]


@app.get("/items/{item_id}/public", response_model=Item02, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items02[item_id]


@app.get(
    "/items/{item_id}/name01",
    response_model=Item02,
    response_model_include=["name", "description"],
)
async def read_item_name(item_id: str):
    return items02[item_id]


@app.get("/items/{item_id}/public01", response_model=Item02, response_model_exclude=["tax"])
async def read_item_public_data(item_id: str):
    return items02[item_id]
