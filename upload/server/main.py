from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to file server"}


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    print(file)
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(file.filename)
    return {"filename": file.filename}