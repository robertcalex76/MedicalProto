from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..db.models import NursingHome
from ..db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/nursing_homes/", response_model=List[NursingHome])
def get_nursing_homes(state: Optional[str] = None, rating: Optional[float] = None, ownership_type: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(NursingHome)
    
    if state:
        query = query.filter(NursingHome.state == state)
    if rating:
        query = query.filter(NursingHome.rating >= rating)
    if ownership_type:
        query = query.filter(NursingHome.ownership_type == ownership_type)
    
    nursing_homes = query.all()
    
    if not nursing_homes:
        raise HTTPException(status_code=404, detail="No nursing homes found")
    
    return nursing_homes

@router.get("/nursing_homes/{nursing_home_id}", response_model=NursingHome)
def get_nursing_home(nursing_home_id: int, db: Session = Depends(get_db)):
    nursing_home = db.query(NursingHome).filter(NursingHome.id == nursing_home_id).first()
    
    if nursing_home is None:
        raise HTTPException(status_code=404, detail="Nursing home not found")
    
    return nursing_home