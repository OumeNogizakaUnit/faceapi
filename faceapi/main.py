from typing import Optional

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from faceapi import __name__ as name
from faceapi.utils import find_face, predict, save_temp_file

app = FastAPI()

origins = [
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


@app.post("/api/v1/locations")
def image_locations(
        file: UploadFile = File(...)):
    '''画像から顔識別

    Keyword Arguments:
        file UploadFile -- 画像ファイル

    Returns:
        List[List] -- 識別された顔の場所のリスト
    '''
    filepath = save_temp_file(file)
    locations = find_face(filepath)
    res = {"result": locations}
    print(res)
    return res


@app.post("/api/v1/perdict")
def image_predict(
        file: UploadFile = File(...),
        modelid: Optional[int] = 0):
    '''画像から指定されたモデルを利用して顔判別

    Keyword Arguments:
        file UploadFile -- 画像ファイル
        modelid Optional[int] -- 利用するモデルのID

    Returns:
        Dict[List] -- 判別結果

    '''
    filepath = save_temp_file(file)
    locations = predict(filepath)
    res = {"result": locations}
    return res


@app.get("/api/v1/models")
def list_models():
    model_list = [{'id': 0, 'modelname': 'model.sav', 'memberlist': ['member1', 'member2']}]
    return {"result": model_list}


@app.get("/api/v1/models/{modelid}")
def get_model(
        modelid: Optional[int]):
    return modelid
