from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from typing import List

from .. import utils
from ..models.database import ApiSession
from ..models.images import Image 
from ..schemas.images_schema import ImageBase

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
    image_urls = [utils.upload_to_firebase(file) for file in files]
    # Get random tracks from spotify for each file
    random_tracks = [utils.get_random_track() for file in files]

    # Create records with data
    db_images = []
    for i in range(len(files)):
        db_images.append(Image())
        db_images = [Image(
            image_url=image_urls[i],
            spotify_name=random_tracks[0].name,
            spotify_uri=random_tracks[0].uri,
            spotify_preview_url=random_tracks[0].preview_url,
            spotify_popularity=random_tracks[0].popularity,
        )]

    # Save to db
    db.add_all(db_images)
    db.commit()
    return db_images
