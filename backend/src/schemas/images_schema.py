from typing import List, Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    id: int
    url: str
    full_url: str

    class Config:
        orm_mode = True

