from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from datetime import timedelta


def get_single(id:int, db: Session):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id).first()
    return reservation


def get_all(db: Session):
    reservations = db.query(models.Reservation).all()
    return reservations


def create(request: schemas.Reservation, db: Session):
    new_start = request.reservation_time
    new_end = new_start + timedelta(minutes=request.duration_minutes)

    existing_reservations = db.query(models.Reservation).filter(
        models.Reservation.table_id == request.table_id
    ).all()

    for reservation in existing_reservations:
        existing_start = reservation.reservation_time
        existing_end = existing_start + timedelta(minutes=reservation.duration_minutes)

        if new_start < existing_end and new_end > existing_start:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Столик уже занят в указанный временной интервал"
            )

    reservation = models.Reservation(
        customer_name=request.customer_name,
        table_id=request.table_id,
        reservation_time=request.reservation_time,
        duration_minutes=request.duration_minutes
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


def delete(id: int, db: Session):
    reservation = db.query(models.Reservation).filter(models.Reservation.id == id).first()

    if not reservation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Брони с id {id} не существует.'
                            )

    db.delete(reservation)
    db.commit()
    return schemas.DeleteResponse(message=f"Бронь с id-{id} успешно удалена")
