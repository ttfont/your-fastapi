from fastapi import FastAPI

description = """
YourApp API helps you do awesome stuff. 

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

# openapi_url=None 完全禁用 OpenAPI 模式
app = FastAPI(
    title="这是一个 title",
    description=description,
    summary="这是一个 summary ",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "这是 contact name ",
        "url": "http:/your.com/contact/",
        "email": "your@fast.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }, openapi_tags=tags_metadata, openapi_url="/api/v1/openapi.json", docs_url="/your_docs", redoc_url=None
)


@app.get("/items/")
async def read_items():
    return [{"name": "Katana"}]


@app.get("/users01/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items02/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
