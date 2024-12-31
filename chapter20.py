from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@app.post("/files01/")
async def create_file01(file: bytes | None = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile01/")
async def create_upload_file01(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


@app.post("/files02/")
async def create_file02(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile02/")
async def create_upload_file02(
        file: UploadFile = File(description="A file read as UploadFile"), ):
    return {"filename": file.filename}


@app.post("/files03/")
async def create_files03(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles03/")
async def create_upload_files03(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files03/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles03/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/files04/")
async def create_files04(
    files: list[bytes] = File(description="Multiple files as bytes"),
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles04/")
async def create_upload_files04(
    files: list[UploadFile] = File(description="Multiple files as UploadFile"),
):
    return {"filenames": [file.filename for file in files]}


@app.get("/index")
async def main():
    content = """
<body>
<form action="/files04/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles04/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)