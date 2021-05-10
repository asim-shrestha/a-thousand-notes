from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, File
from typing import List

from ..models.database import ApiSession
from ..schemas.images_schema import ImageReturn

from . import image_service

router = APIRouter()

@router.get("/", response_model=List[ImageReturn])
def get_all_images(db: Session = Depends(ApiSession)):
    return image_service.get_all_images(db)

@router.get("/{image_id}", response_model=ImageReturn)
def get_image_by_id(image_id: int, db: Session = Depends(ApiSession)):
    return image_service.get_image_by_id(image_id, db)

@router.post("/name/{image_name}", response_model=List[ImageReturn])
def create_images(image_name: str, files: List[bytes] = File(...), db: Session = Depends(ApiSession)):
    return image_service.create_images(image_name, files, db)

@router.delete("/{image_id}", response_model=None)
def delete_image_by_id(image_id: int, db: Session = Depends(ApiSession)):
    return image_service.delete_image_by_id(image_id, db)

@router.delete("/", response_model=None)
def delete_images_by_ids(image_ids: List[int], db: Session = Depends(ApiSession)):
    return image_service.delete_images_by_ids(image_ids, db)