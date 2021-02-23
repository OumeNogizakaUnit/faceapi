from pathlib import Path
from typing import List, NamedTuple, TypedDict

from pydantic import BaseModel

MEMBER_LIST = List[str]


class ModelBase(BaseModel):
    name: str
    description: str
    member_list: MEMBER_LIST
    filepath: Path

    class Config:
        orm_mode = True


class CreateModel(BaseModel):
    name: str
    description: str
    member_list: MEMBER_LIST
    filepath: str


class FaceLocation(NamedTuple):
    x1: int
    y1: int
    x2: int
    y2: int


class Result(TypedDict):
    name: str
    matchrate: float
