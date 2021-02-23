from sqlalchemy.orm import Session

from faceapi.schema import CreateModel
from faceapi.backend.models import Model, memberlist2str


def create_model(db: Session, model: CreateModel):
    m = Model(name=model.name,
              description=model.description,
              filepath=model.filepath,
              member_list=memberlist2str(model.member_list))
    db.add(m)
    db.commit()
    db.refresh(m)
    return m


def get_model(db: Session, model_id: int):
    return db.query(Model).filter(Model.model_id == model_id).first()


def list_models(db: Session, limit=100):
    return db.query(Model).limit(limit).all()


def delete_model(db: Session, model_id: int):
    m = get_model(db, model_id)
    db.delete(m)
    db.commit()
    db.refresh(m)
    return model_id
