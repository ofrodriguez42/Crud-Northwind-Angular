import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def test_db():
    session = Session()
    yield session
    session.close()

def test_create_order_detail():
    order_detail_data = {
        "OrderID": 10248,
        "ProductID": 11,
        "UnitPrice": 14.0,
        "Quantity": 12,
        "Discount": 0.0
    }

    response = client.post("/order-details/", json=order_detail_data)
    assert response.status_code == 200
    assert response.json()["OrderID"] == 10248

def test_read_order_detail():
    response = client.get("/order-details/10248/11")
    assert response.status_code == 200
    assert response.json()["OrderID"] == 10248
    assert response.json()["ProductID"] == 11

def test_update_order_detail():
    order_detail_update_data = {
        "Quantity": 15
    }

    response = client.put("/order-details/10248/11", json=order_detail_update_data)
    assert response.status_code == 200
    assert response.json()["Quantity"] == 15

def test_delete_order_detail():
    response = client.delete("/order-details/10248/11")
    assert response.status_code == 200
    assert response.json()["detail"] == "Order Detail deleted successfully"
