from sqlalchemy.orm import Session
from models.orders import Orders
from fastapi import HTTPException
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_order(order_data: dict, db: Session):
    try:
        new_order = Orders(**order_data)
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        return new_order
    except Exception as e:
        db.rollback()
        logger.error(f"Error al crear la orden: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def get_order_by_id(order_id: int, db: Session):
    return db.query(Orders).filter(Orders.OrderID == order_id).first()

def update_order(order_id: int, order_data: dict, db: Session):
    existing_order = get_order_by_id(order_id, db)
    if existing_order is None:
        return None
    try:
        for key, value in order_data.items():
            setattr(existing_order, key, value)
        db.commit()
        db.refresh(existing_order)
        return existing_order
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete_order(order_id: int, db: Session):
    existing_order = get_order_by_id(order_id, db)
    if existing_order is None:
        return False
    try:
        db.delete(existing_order)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))