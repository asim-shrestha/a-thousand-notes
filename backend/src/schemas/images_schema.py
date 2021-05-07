from typing import List, Optional

from pydantic import BaseModel


class ImageBase(BaseModel):
    url: str

