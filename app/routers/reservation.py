from fastapi import APIRouter, Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..services import reservation

router = APIRouter(
    prefix="/reservations",
    tags=['reservations']
)


@router.get("/", response_model=List[schemas.Reservation])
def get_reservations(db: Session = Depends(database.get_db)) -> List[str]:
    return reservation.get_all(db)


@router.get("/{id}", response_model=schemas.Reservation)
def get_single_reservation(id: int, db: Session = Depends(database.get_db)):
    return reservation.get_single(id, db)


@router.post("/", response_model=schemas.Reservation)
def create_table(request: schemas.Reservation, db: Session = Depends(database.get_db)):
    return reservation.create(request, db)


@router.delete("/{id}", response_model=schemas.DeleteResponse)
def delete_table(id: int, db: Session = Depends(database.get_db)):
    return reservation.delete(id, db)
