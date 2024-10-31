from fastapi import FastAPI

#  uvicorn chapter01:app --reload 启动
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World！ app"}

#  uvicorn chapter01:my_awesome_api --reload 启动
my_awesome_api = FastAPI()


@my_awesome_api.get("/")
async def root():
    return {"message": "Hello World！my_awesome_api"}