from typing import Optional
from fastapi import FastAPI, File, UploadFile

from faceapi import __name__ as name
from faceapi.utils import (save_temp_file,
                           predict)


app = FastAPI()


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
    locations = predict(filepath)
    print(locations)
    return {"type1": locations}
