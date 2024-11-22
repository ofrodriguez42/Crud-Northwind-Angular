from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.orders_service import create_order, get_order_by_id, update_order, delete_order
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

class OrderCreate(BaseModel):
    CustomerID: str
    EmployeeID: int
    OrderDate: str
    RequiredDate: str
    ShippedDate: str
    ShipVia: int
    Freight: float
    ShipName: str
    ShipAddress: str
    ShipCity: str
    ShipRegion: str
    ShipPostalCode: str
    ShipCountry: str

class OrderUpdate(BaseModel):
    CustomerID: str = None
    EmployeeID: int = None
    OrderDate: str = None
    RequiredDate: str = None
    ShippedDate: str = None
    ShipVia: int = None
    Freight: float = None
    ShipName: str = None
    ShipAddress: str = None
    ShipCity: str = None
    ShipRegion: str = None
    ShipPostalCode: str = None
    ShipCountry: str = None

@router.post("/")
def create_order_endpoint(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(order.dict(), db)

@router.get("/{order_id}")
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = get_order_by_id(order_id, db)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}")
def update_order_endpoint(order_id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    updated_order = update_order(order_id, order.dict(exclude_unset=True), db)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@router.delete("/{order_id}")
def delete_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    if not delete_order(order_id, db):
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted successfully"}
