from fastapi.testclient import TestClient  # 导入 TestClient 用于测试 FastAPI 应用

from .main import app  # 导入 FastAPI 应用实例

client = TestClient(app)  # 创建 TestClient 实例，传入 FastAPI 应用


# 测试根路径 GET 请求，验证返回内容
def test_read_main():
    response = client.get("/")  # 发送 GET 请求到根路径
    assert response.status_code == 200  # 验证返回状态码为 200
    assert response.json() == {"msg": "Hello World"}  # 验证返回内容是否正确


# 测试 GET 请求，带有有效的 X-Token 头部，验证返回内容
def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})  # 发送带有 Token 的 GET 请求
    assert response.status_code == 200  # 验证返回状态码为 200
    assert response.json() == {  # 验证返回内容是否与预期一致
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }


# 测试 GET 请求，带有无效的 X-Token 头部，验证返回错误信息
def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})  # 发送带有无效 Token 的 GET 请求
    assert response.status_code == 400  # 验证返回状态码为 400
    assert response.json() == {"detail": "Invalid X-Token header"}  # 验证错误信息


# 测试 GET 请求，查询不存在的项目，验证返回 404 错误
def test_read_nonexistent_item():
    response = client.get("/items/baz", headers={"X-Token": "coneofsilence"})  # 发送 GET 请求查询不存在的项
    assert response.status_code == 404  # 验证返回状态码为 404
    assert response.json() == {"detail": "Item not found"}  # 验证错误信息


# 测试 POST 请求，创建新项目，验证返回内容
def test_create_item():
    response = client.post(
        "/items/",  # 发送 POST 请求到 /items 路径
        headers={"X-Token": "coneofsilence"},  # 包含有效的 X-Token 头部
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},  # 请求体内容
    )
    assert response.status_code == 200  # 验证返回状态码为 200
    assert response.json() == {  # 验证返回的内容是否正确
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


# 测试 POST 请求，使用无效的 X-Token 创建新项目，验证返回错误信息
def test_create_item_bad_token():
    response = client.post(
        "/items/",  # 发送 POST 请求到 /items 路径
        headers={"X-Token": "hailhydra"},  # 使用无效的 Token
        json={"id": "bazz", "title": "Bazz", "description": "Drop the bazz"},  # 请求体内容
    )
    assert response.status_code == 400  # 验证返回状态码为 400
    assert response.json() == {"detail": "Invalid X-Token header"}  # 验证错误信息


# 测试 POST 请求，尝试创建已存在的项目，验证返回 409 错误
def test_create_existing_item():
    response = client.post(
        "/items/",  # 发送 POST 请求到 /items 路径
        headers={"X-Token": "coneofsilence"},  # 包含有效的 X-Token 头部
        json={  # 请求体内容，尝试创建已存在的项
            "id": "foo",
            "title": "The Foo ID Stealers",
            "description": "There goes my stealer",
        },
    )
    assert response.status_code == 409  # 验证返回状态码为 409
    assert response.json() == {"detail": "Item already exists"}  # 验证错误信息
