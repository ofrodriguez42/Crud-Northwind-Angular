# models/orders.py
from sqlalchemy import Column, Integer, String, DateTime, Float
from models.base import Base  # Importar Base desde base.py

class Orders(Base):
    __tablename__ = 'Orders'  # Nombre exacto de la tabla en la base de datos
    OrderID = Column(Integer, primary_key=True, index=True)
    CustomerID = Column(String(5), nullable=True)
    EmployeeID = Column(Integer, nullable=True)
    OrderDate = Column(DateTime, nullable=True)
    RequiredDate = Column(DateTime, nullable=True)
    ShippedDate = Column(DateTime, nullable=True)
    ShipVia = Column(Integer, nullable=True)
    Freight = Column(Float, nullable=True)
    ShipName = Column(String(40), nullable=True)
    ShipAddress = Column(String(60), nullable=True)
    ShipCity = Column(String(15), nullable=True)
    ShipRegion = Column(String(15), nullable=True)
    ShipPostalCode = Column(String(10), nullable=True)
    ShipCountry = Column(String(15), nullable=True)