from sqlalchemy.schema import Column
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import DateTime, Integer, String

from faceapi.backend import Base, Engine
from faceapi.schema import MEMBER_LIST


class Model(Base):
    __tablename__ = "model"
    model_id = Column(Integer,
                      primary_key=True,
                      autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    member_list = Column(String(255), nullable=False)
    filepath = Column(String(255), nullable=False)
    create_at = Column(DateTime, server_default=current_timestamp())

    def get_member_list(self) -> MEMBER_LIST:
        return self.member_list.split(',')


def memberlist2str(member_list: MEMBER_LIST) -> str:
    return ','.join([str(m) for m in member_list])


def init_database():
    Base.metadata.create_all(bind=Engine)
