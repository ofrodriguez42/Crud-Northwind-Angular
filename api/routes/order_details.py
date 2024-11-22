from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.order_details_service import create_order_detail, get_order_detail_by_id, update_order_detail, delete_order_detail
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

class OrderDetailCreate(BaseModel):
    OrderID: int
    ProductID: int
    UnitPrice: float
    Quantity: int
    Discount: float

class OrderDetailUpdate(BaseModel):
    UnitPrice: float = None
    Quantity: int = None
    Discount: float = None

@router.post("/")
def create_order_detail_endpoint(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return create_order_detail(order_detail.dict(), db)

@router.get("/{order_id}/{product_id}")
def read_order_detail(order_id: int, product_id: int, db: Session = Depends(get_db)):
    order_detail = get_order_detail_by_id(order_id, product_id, db)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_detail

@router.put("/{order_id}/{product_id}")
def update_order_detail_endpoint(order_id: int, product_id: int, order_detail: OrderDetailUpdate, db: Session = Depends(get_db)):
    updated_order_detail = update_order_detail(order_id, product_id, order_detail.dict(exclude_unset=True), db)
    if updated_order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return updated_order_detail

@router.delete("/{order_id}/{product_id}")
def delete_order_detail_endpoint(order_id: int, product_id: int, db: Session = Depends(get_db)):
    if not delete_order_detail(order_id, product_id, db):
        raise HTTPException(status_code=404, detail="Order detail not found")
    return {"detail": "Order detail deleted successfully"}