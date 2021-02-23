from typing import Optional

from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from faceapi import __name__ as name
from faceapi.backend import SessionLocal
from faceapi.backend.utils import create_model, get_model, list_models
from faceapi.schema import CreateModel
from faceapi.utils import find_face, predict, save_model_file, save_temp_file

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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"This is": name}


@app.post("/api/v1/locations")
def api_image_locations(
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
    return res


@app.post("/api/v1/perdict")
def api_image_predict(
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
def api_list_models(db: Session = Depends(get_db)):
    model_list = list_models(db)
    return {"result": model_list}


@app.post("/api/v1/models/upload")
def api_upload_model(file: UploadFile = File(...)):
    filepath = save_model_file(file)
    return {"filepath": filepath}


@app.post("/api/v1/models")
def api_create_model(
        modeldata: CreateModel,
        db: Session = Depends(get_db)):
    result = modeldata.name
    try:
        create_model(db, modeldata)
    except Exception as error:
        result = str(error)
    return {"result": result}


@app.get("/api/v1/models/{modelid}")
def api_get_model(
        modelid: int,
        db: Session = Depends(get_db)):
    _model = get_model(db, modelid)
    return {"result": _model}
