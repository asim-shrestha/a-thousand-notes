from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..models.images import Image 
from ..schemas.images_schema import ImageBase

router = APIRouter()
@router.get("/{image_id}", response_model=ImageBase)
def get_image(image_id: int, db: Session = Depends(Session)):
    return db.query(Image).filter(Image.id == image_id).first()

@router.post("/", response_model=ImageBase)
def create_image(new_image: ImageBase, db: Session = Depends(Session)):
    db_image = Image(url = new_image.url)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
