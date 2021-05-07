import os
from dotenv import load_dotenv

from fastapi.testclient import TestClient

# Load environment variables and change DB
load_dotenv('../../docker.env')
os.environ['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///./tests.db?check_same_thread=False'

from src import app

client = TestClient(app)