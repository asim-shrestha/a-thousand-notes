from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from typing import List

from ..models.database import ApiSession
from ..models.images import Image 
from ..schemas.images_schema import ImageBase

from PIL import Image as PILImage
import io
from . import image_service

router = APIRouter()

@router.get("/{image_id}", response_model=ImageBase)
def get_image_by_id(image_id: int, db: Session = Depends(ApiSession)):
    return image_service.get_image_by_id(image_id, db)

@router.post("/", response_model=List[ImageBase])
def create_images(files: List[bytes] = File(...), db: Session = Depends(ApiSession)):
    return image_service.create_images(files, db)

@router.delete("/{image_id}", response_model=None)
def delete_images_by_ids(image_id: int, db: Session = Depends(ApiSession)):
    return image_service.delete_images_by_ids(image_id, db)