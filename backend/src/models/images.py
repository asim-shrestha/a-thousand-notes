from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String)
    image_url = Column(String)

    spotify_name = Column(String)
    spotify_uri = Column(String)
    spotify_preview_url = Column(String)
    spotify_popularity = Column(String)