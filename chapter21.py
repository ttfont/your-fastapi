from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files01/")
async def create_file(
        file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
