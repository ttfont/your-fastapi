from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
        q: str = Depends(query_extractor),
        last_query: str | None = Cookie(default=None)):
    if not q:
        return last_query
    return q


@app.get("/items01/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}
