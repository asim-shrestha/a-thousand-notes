from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    full_url = Column(String)