from fastapi import FastAPI  # 导入 FastAPI 类
from fastapi.staticfiles import StaticFiles  # 导入 StaticFiles，用于提供静态文件

app = FastAPI()  # 创建 FastAPI 应用实例

# 挂载静态文件服务
# 将 StaticFiles 实例挂载到 "/static" 路径，所有以 "/static" 开头的请求都会由 StaticFiles 处理
# directory="static" 指定静态文件所在的目录，这里是名为 "static" 的目录
# name="static" 提供给这个挂载点的内部名称，便于应用内部引用
app.mount("/static", StaticFiles(directory="static"), name="static")