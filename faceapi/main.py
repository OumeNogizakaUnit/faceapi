from typing import Optional
from fastapi import FastAPI, File, UploadFile

from faceapi import __name__ as name
from faceapi.utils import (save_temp_file,
                           predict)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"This is": name}


@app.post("/api/v1/recognition")
def image_predict(
        file: UploadFile = File(...),
        modelid: Optional[int] = 0):
    '''画像から顔識別

    Keyword Arguments:
        file UploadFile -- ファイル情報
        modelid Optional[int] -- 利用するモデルのID

    Returns:
        List[List] -- 識別された顔の場所のリスト

    '''
    filepath = save_temp_file(file)
    print(filepath)
    locations = predict(filepath)
    res = {"type1": locations}
    print(res)
    return res
