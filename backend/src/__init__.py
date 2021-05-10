from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import os
from . import models
from .models import database

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title='A Thousand Notes',
    docs_url='/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("API_CORS_ALLOW_ORIGINS")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/app")
async def redirect_to_front_end():
    response = RedirectResponse(url=os.environ.get("API_CORS_ALLOW_ORIGINS"))
    return response

from . import routes