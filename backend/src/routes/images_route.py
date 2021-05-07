from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from typing import List

from .. import utils
from ..models.database import ApiSession
from ..models.images import Image 
from ..schemas.images_schema import ImageBase

import filetype

router = APIRouter()
@router.get("/{image_id}", response_model=ImageBase)
def get_image(image_id: int, db: Session = Depends(ApiSession)):
    image = db.query(Image).filter(Image.id == image_id).first()
    if image:
        return image
    else:
        raise HTTPException(status_code=404, detail="Image not found")


@router.post("/", response_model=List[dict])
def create_images(files: List[bytes] = File(...), db: Session = Depends(ApiSession)):
    # for file in files:
    #     print(file.content_type)
    #     if not filetype.is_image(file.file):
    #         raise HTTPException(status_code=400, detail="You have uploaded one or more invalid images. Aborting")

    print("Going to upload")
    image_url_dicts = [utils.upload_to_firebase(file) for file in files]
    return image_url_dicts
