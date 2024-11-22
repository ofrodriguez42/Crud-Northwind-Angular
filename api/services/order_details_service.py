from sqlalchemy.orm import Session
from models.order_details import OrderDetails
from fastapi import HTTPException
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_order_detail(order_detail_data: dict, db: Session):
    try:
        logger.info(f"Datos recibidos para OrderDetail: {order_detail_data}")
        new_order_detail = OrderDetails(**order_detail_data)
        db.add(new_order_detail)
        db.commit()
        db.refresh(new_order_detail)
        return new_order_detail
    except Exception as e:
        db.rollback()
        logger.error(f"Error al crear OrderDetail: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def get_order_detail_by_id(order_id: int, product_id: int, db: Session):
    return db.query(OrderDetails).filter(OrderDetails.OrderID == order_id, OrderDetails.ProductID == product_id).first()

def update_order_detail(order_id: int, product_id: int, order_detail_data: dict, db: Session):
    existing_order_detail = get_order_detail_by_id(order_id, product_id, db)
    if existing_order_detail is None:
        return None
    try:
        for key, value in order_detail_data.items():
            setattr(existing_order_detail, key, value)
        db.commit()
        db.refresh(existing_order_detail)
        return existing_order_detail
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete_order_detail(order_id: int, product_id: int, db: Session):
    existing_order_detail = get_order_detail_by_id(order_id, product_id, db)
    if existing_order_detail is None:
        return False
    try:
        db.delete(existing_order_detail)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))