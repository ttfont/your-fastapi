from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item


@app.post("/items01/", response_model=Item, tags=["这是功能A接口"])
async def create_item(item: Item):
    return item


@app.get("/items02/", tags=["这是功能A接口"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users03/", tags=["这是用户A接口"])
async def read_users():
    return [{"username": "johndoe"}]


@app.post(
    "/items03/",
    response_model=Item,
    summary="这是一个items03接口",
    description="这是一个items03接口，它的作用是...",
)
async def create_item(item: Item):
    return item


@app.post("/items04/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    这是简述：
    - **name**：名称
    - **description**：描述
    - **price**：价格
    - **tax**：税费
    - **tags**：标签
    """
    return item


@app.post(
    "/items05/",
    response_model=Item,
    summary="这是一个 summary",
    description="这是一个 description",
    response_description="这是一个 response_description",
)
async def create_item(item: Item):
    """
    这是简述：
    - **name**：名称
    - **description**：描述
    - **price**：价格
    - **tax**：税费
    - **tags**：标签
    """
    return item


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]
