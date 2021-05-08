from typing import List, Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    id: int
    image_url: str

    spotify_name: str
    spotify_uri: str
    spotify_preview_url: str
    spotify_popularity: str

    class Config:
        orm_mode = True

