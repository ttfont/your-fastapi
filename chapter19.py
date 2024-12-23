from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


class FormData01(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}


@app.post("/login/")
async def login(data: FormData = Form()):
    return data


@app.post("/login01/")
async def login01(data: FormData01 = Form()):
    return data


@app.post("/login02/")
async def login(username: str = Form(...), password: str = Form(...)):
    form_data = FormData(username=username, password=password)
    return form_data
