from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from .models import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title='A Thousand Notes',
    docs_url='/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_ALLOW_ORIGINS")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from . import routes