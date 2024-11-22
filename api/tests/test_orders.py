import pytest
from fastapi.testclient import TestClient
from main import app
from database import Session
from models import Orders

client = TestClient(app)

@pytest.fixture
def test_db():
    session = Session()
    yield session
    session.close()

def test_create_order():
    order_data = {
        "CustomerID": "VINET",
        "EmployeeID": 1,
        "OrderDate": "2024-10-01T00:00:00",
        "RequiredDate": "2024-10-10T00:00:00",
        "ShippedDate": "2024-10-05T00:00:00",
        "ShipVia": 1,
        "Freight": 32.38,
        "ShipName": "Vins et alcools Chevalier",
        "ShipAddress": "59 rue de l'Abbaye",
        "ShipCity": "Reims",
        "ShipRegion": "NA",
        "ShipPostalCode": "51100",
        "ShipCountry": "France"
    }

    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    assert response.json()["CustomerID"] == "VINET"

def test_read_order():
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json()["OrderID"] == 1

def test_update_order():
    order_update_data = {
        "Freight": 50.00
    }

    response = client.put("/orders/1", json=order_update_data)
    assert response.status_code == 200
    assert response.json()["Freight"] == 50.00

def test_delete_order():
    response = client.delete("/orders/1")
    assert response.status_code == 200
    assert response.json()["detail"] == "Order deleted successfully"
