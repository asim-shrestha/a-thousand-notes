from fastapi import Depends
from src import app
from . import images_route


app.include_router(images_route.router, tags=['Images'], prefix='/image')