from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE = 'sqlite:///db.sqlite3'

Engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=Engine)
