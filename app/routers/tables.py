from fastapi import APIRouter, Depends
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..services import tables

router = APIRouter(
    prefix="/tables",
    tags=['tables']
)


@router.get("/", response_model=List[schemas.Table])
def get_tables(db: Session = Depends(database.get_db)) -> List[str]:
    return tables.get_all(db)


@router.post("/", response_model=schemas.Table)
def create_table(request: schemas.Table, db: Session = Depends(database.get_db)):
    return tables.create(request, db)


@router.delete("/{id}", response_model=schemas.DeleteResponse)
def delete_table(id: int, db: Session = Depends(database.get_db)):
    return tables.delete(id, db)
