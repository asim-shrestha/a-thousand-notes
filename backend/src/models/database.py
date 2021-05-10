import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_url = os.environ.get('DATABASE_URL')
# Apply fix for heroku
if engine_url.startswith('postgres:'):
    engine_url = engine_url.replace('postgres', 'postgresql')

print(engine_url)
engine = create_engine(engine_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def ApiSession():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

Base = declarative_base()