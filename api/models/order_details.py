# models/order_details.py
from sqlalchemy import Column, Integer, Float, SmallInteger, ForeignKey, PrimaryKeyConstraint
from models.base import Base

class OrderDetails(Base):
    __tablename__ = 'Order Details'  # Nombre exacto de la tabla con espacio
    OrderID = Column(Integer, ForeignKey('Orders.OrderID'), nullable=False)
    ProductID = Column(Integer, nullable=False)
    UnitPrice = Column(Float, nullable=False, default=0)
    Quantity = Column(SmallInteger, nullable=False, default=1)
    Discount = Column(Float, nullable=False, default=0)

    __table_args__ = (
        PrimaryKeyConstraint('OrderID', 'ProductID', name='PK_Order_Details'),
    )