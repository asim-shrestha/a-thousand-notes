from typing import List, Optional

from pydantic import BaseModel

class AppBase(BaseModel):
    class Config:
        orm_mode = True

class ImageReturn(AppBase):
    id: int
    image_name: str
    image_url: str

    spotify_name: str
    spotify_uri: str
    spotify_preview_url: str