from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, File
from typing import List

from .. import utils
from ..models.database import ApiSession
from ..models.images import Image 

from PIL import Image as PILImage
import io

def get_all_images(db: Session):
    return db.query(Image).all()

def get_image_by_id(image_id: int, db: Session):
    image = db.query(Image).filter(Image.id == image_id).first()
    if image:
        return image
    else:
        raise HTTPException(status_code=404, detail="Image not found")

def create_images(image_name: str, files: List[bytes] = File(...), db: Session = Depends(ApiSession)):
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
            image_name=image_name,
            image_url=image_urls[i],
            spotify_name=random_tracks[0].name,
            spotify_uri=random_tracks[0].uri,
            spotify_preview_url=random_tracks[0].preview_url,
        )]

    # Save to db
    db.add_all(db_images)
    db.commit()
    return db_images
    
def delete_images_by_ids(image_id: int, db: Session):
    image = get_image_by_id(image_id, db)
    db.delete(image)
    db.commit()
    return