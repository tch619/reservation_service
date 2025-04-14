from pydantic import BaseModel, field_validator
from datetime import datetime


class Table(BaseModel):
    id: int | None = None
    name: str
    seats: int
    location: str


class Reservation(BaseModel):
    id: int | None = None
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

    @field_validator("reservation_time", mode='before')
    def parse_reservation_time(cls, value):
        if isinstance(value, datetime):
            return value
        for fmt in ("%d.%m.%y %H:%M", "%Y-%m-%dT%H:%M:%S"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
        raise ValueError("Неверный формат даты. Допустимые: '21.04.25 13:30' или '2025-04-21T13:30:00'")


class DeleteResponse(BaseModel):
    message: str
