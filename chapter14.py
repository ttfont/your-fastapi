from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}


@app.get("/items02/")
async def read_items(
        strange_header: str | None = Header(default=None, convert_underscores=False), ):
    return {"strange_header": strange_header}


@app.get("/items03/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items04/")
async def read_items(headers: CommonHeaders = Header()):
    return headers


class CommonHeaders02(BaseModel):
    model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items05/")
async def read_items(headers: CommonHeaders02 = Header()):
    return headers
