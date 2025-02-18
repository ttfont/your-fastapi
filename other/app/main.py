from fastapi import FastAPI, Header, HTTPException  # 导入 FastAPI，Header 和 HTTPException
from pydantic import BaseModel  # 导入 Pydantic 的 BaseModel，用于数据验证

app = FastAPI()  # 创建 FastAPI 应用实例


@app.get("/")  # 定义根路径的 GET 请求处理函数
async def read_main():
    return {"msg": "Hello World"}  # 返回简单的 JSON 响应


# 模拟的 "secret token"，用于验证请求头中的 X-Token
fake_secret_token = "coneofsilence"

# 模拟的数据库，存储一些项目数据
fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}


# 定义 Item 模型，使用 Pydantic 的 BaseModel 进行数据验证
class Item(BaseModel):
    id: str  # 项目的唯一 ID
    title: str  # 项目的标题
    description: str | None = None  # 项目的描述，默认为 None


@app.get("/items/{item_id}", response_model=Item)  # 定义 GET 请求路径，返回一个 Item
async def read_item(item_id: str, x_token: str = Header()):  # 接受路径参数 item_id 和请求头中的 X-Token
    if x_token != fake_secret_token:  # 检查 X-Token 是否有效
        raise HTTPException(status_code=400, detail="Invalid X-Token header")  # 无效时抛出 400 错误
    if item_id not in fake_db:  # 检查 item_id 是否存在于 fake_db 中
        raise HTTPException(status_code=404, detail="Item not found")  # 不存在时抛出 404 错误
    return fake_db[item_id]  # 返回对应的项目


@app.post("/items/", response_model=Item)  # 定义 POST 请求路径，用于创建一个新项目
async def create_item(item: Item, x_token: str = Header()):  # 接受请求体中的 item 和请求头中的 X-Token
    if x_token != fake_secret_token:  # 检查 X-Token 是否有效
        raise HTTPException(status_code=400, detail="Invalid X-Token header")  # 无效时抛出 400 错误
    if item.id in fake_db:  # 检查 item.id 是否已经存在于 fake_db 中
        raise HTTPException(status_code=409, detail="Item already exists")  # 已存在时抛出 409 错误
    fake_db[item.id] = item  # 将新的项目添加到 fake_db 中
    return item  # 返回创建的项目
