from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    tables = db.query(models.Table).all()
    return tables


def create(request: schemas.Table, db: Session):
    new_table = models.Table(name=request.name, seats=request.seats, location=request.location)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


def delete(id: int, db: Session):
    tables = db.query(models.Table).filter(models.Table.id == id).first()

    if not tables:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Столика с id {id} не существует.'
                            )
    db.delete(tables)
    db.commit()
    return {"message": f"Стол с id-{id} успешно удален"}
