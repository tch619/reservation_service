from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from .database import (Base)
from sqlalchemy.orm import relationship


class Table(Base):
    __tablename__ = 'table'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    seats = Column(Integer)
    location = Column(String)

    reservations = relationship("Reservation", back_populates="table")


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    table_id = Column(Integer, ForeignKey('table.id'))
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)

    table = relationship("Table", back_populates="reservations")
