import pytest
from sqlalchemy_utils import drop_database, create_database, database_exists

from src.models.database import Base, engine


@pytest.fixture(scope="function", autouse=True)
def create_test_database():
    # Ensure the DB engine is a test DB
    url = engine.url
    assert 'test' in str(url)

    if database_exists(url):
        drop_database(url)

    create_database(engine.url)
    Base.metadata.create_all(bind=engine)

    yield