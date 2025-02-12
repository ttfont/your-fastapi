import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    # 自定义请求头
    # 若要在浏览器客户端中看到自定义请求头，将其添加到 CORS 配置的 expose_headers 参数中
    response.headers["X-Process-Time"] = str(process_time)  # 单位（秒）
    return response


@app.get("/items01/{item_id}")
async def read_user_item(item_id: str):
    item = {"item_id": item_id}
    return item
