from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
        item_id: int = Path(title="这是一个路径参数"),
        q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items02/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="这是一个路径参数02")],
        q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items03/{item_id}")
async def read_items(*, item_id: int = Path(title="这是一个路径参数03"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items04/{item_id}")
async def read_items(
        *, item_id: int = Path(title="这是一个路径参数04", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items05/{item_id}")
async def read_items(
        *,
        item_id: int = Path(title="这是一个路径参数05", gt=0, le=1000),
        q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items06/{item_id}")
async def read_items(
        *,
        item_id: int = Path(title="这是一个路径参数06", ge=0, le=1000),
        q: str,
        size: float = Query(gt=0, lt=10.5),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results
