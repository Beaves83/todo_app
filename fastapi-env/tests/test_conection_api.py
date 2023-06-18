import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item():
    item = {"title": "Test Item", "description": "This is a test item"}
    response = client.post("/items", json=item)
    assert response.status_code == 200
    assert response.json() == {"message": "Item created successfully"}

def test_update_item():
    item = {"title": "Updated Item", "description": "This is an updated item", "completed": True}
    response = client.put("/items/1", json=item)
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 updated successfully"}

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 deleted successfully"}