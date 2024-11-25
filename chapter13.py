from fastapi import Cookie, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cookies(BaseModel):
    session_id: str
    path_tracker: str | None = None
    web_tracker: str | None = None


class Cookies02(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


@app.get("/items01/")
async def read_items(cookies: Cookies = Cookie()):
    return cookies


@app.get("/items02/")
async def read_items(cookies: Cookies02 = Cookie()):
    return cookies
