import os
from dotenv import load_dotenv

from fastapi.testclient import TestClient

# Load environment variables and change DB
ENV_PATH = '../../docker.env'
assert os.path.isfile('../../docker.env'), "Please ensure you are in the tests folder before running tests"

load_dotenv(ENV_PATH)
os.environ['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///./tests.db?check_same_thread=False'
from src import app

client = TestClient(app)