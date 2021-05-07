from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from typing import List

from .. import utils
from ..models.database import ApiSession
from ..models.images import Image 
from ..schemas.images_schema import ImageBase

import filetype
from PIL import Image as PILImage
import io

router = APIRouter()
@router.get("/{image_id}", response_model=ImageBase)
def get_image(image_id: int, db: Session = Depends(ApiSession)):
    image = db.query(Image).filter(Image.id == image_id).first()
    if image:
        return image
    else:
        raise HTTPException(status_code=404, detail="Image not found")


@router.post("/", response_model=List[ImageBase])
def create_images(files: List[bytes] = File(...), db: Session = Depends(ApiSession)):
    # Test if the file is an image by attempting to read it with PIL
    for file in files:
        try:
            PILImage.open(io.BytesIO(file))
        except:
            raise HTTPException(status_code=400, detail="You have uploaded one or more invalid images. Aborting")

    # Upload to firebase and create entities
    image_url_dicts = [utils.upload_to_firebase(file) for file in files]
    db_images = [Image(url=url_dict['url'], full_url = url_dict['full_url']) for url_dict in image_url_dicts]

    # Save to db
    db.add_all(db_images)
    db.commit()
    return db_images