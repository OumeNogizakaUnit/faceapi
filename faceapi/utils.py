import csv
import pickle
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List, NamedTuple, TypedDict

import face_recognition  # type: ignore
from fastapi import UploadFile
from sklearn.svm import SVC  # type: ignore

from faceapi import MODEL_DIR

modelpath = Path(MODEL_DIR, 'rikaorother.sav')
memberlist = Path(MODEL_DIR, 'rikaorother.csv')


class FaceLocation(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int


class Result(TypedDict):
    name: str
    matchrate: float


def find_face(imagefile: Path) -> List[FaceLocation]:
    imagedata = face_recognition.load_image_file(imagefile)
    face_locations: List[FaceLocation] = face_recognition.face_locations(
        imagedata)
    return face_locations


def predict(imagefile: Path) -> List[List[Result]]:
    imagedata = face_recognition.load_image_file(imagefile)
    face_locations = face_recognition.face_locations(imagedata)
    if len(face_locations) == 0:
        return []
    model = _load_model(modelpath)
    categories = _load_categories(memberlist)

    cnv = face_recognition.face_encodings(imagedata,
                                          known_face_locations=face_locations)
    _result_all_face = model.predict_proba(cnv)
    all_result_list: List[List[Result]] = []
    for _result_one_face in _result_all_face:
        result_list: List[Result] = []
        for member, rate in zip(categories, _result_one_face):
            result: Result = {"name": member,
                              "matchrate": round(rate*100, 2)}
            result_list.append(result)
        all_result_list.append(result_list)
    return all_result_list


def _load_categories(csvfilepath: Path) -> List[str]:
    memberlist = []
    with csvfilepath.open('r') as fd:
        reader = csv.reader(fd)
        memberlist = next(reader)
    return memberlist


def _load_model(modelpath: Path) -> SVC:
    model = None
    with modelpath.open('rb') as fd:
        model = pickle.load(fd)
    return model


def save_temp_file(uploadfile: UploadFile) -> Path:
    suffix = Path(uploadfile.filename).suffix
    try:
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(uploadfile.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        uploadfile.file.close()
    return tmp_path
