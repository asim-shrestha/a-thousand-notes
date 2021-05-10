import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def ApiSession():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

Base = declarative_base()