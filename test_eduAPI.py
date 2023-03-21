from fastapi.testclient import TestClient

from eduAPI import app

client = TestClient(app)

# Run the test: pytest

### Get tests

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello World"}

def test_get_item():
    response = client.get("/item/0")
    assert response.status_code == 200
    assert response.json() == {"name" : "name", "description": "description", "price" : 1000}

def test_get_not_inventory_item():
    response = client.get("/item/1") # Puedo poner un -1?
    assert response.status_code == 404
    assert response.json() == {"detail" : "Item ID not found."}

"""def test_get_by_name():
    response = client.get("item/get-by-name?name=name")
    assert response.status_code == 200
    assert response.json() == {"name" : "name", "description": "description", "price" : 1000}

def test_get_by_name_not_inventory():
    response = client.get("item/get-by-name?name=test") # Importa si pongo name = test?
    assert response.status_code == 404
    assert response.json() == {"detail" : "Item name not found."}"""

### Post tests

def test_create_existing_item():
    response = client.post("/create-item/0", json = {"name" : "name", "description": "description", "price" : 1000})
    assert response.status_code == 400
    assert response.json() == {"detail" : "Item ID already exists."}

def test_create_item():
    response = client.post("/create-item/2", json = {"name" : "test", "description": "description", "price" : 0})
    assert response.status_code == 200
    assert response.json() == {"name" : "test", "description": "description", "price" : 0}

### Put tests

def test_update_item():
    response = client.put("/update-item/0", json = {"name" : "test", "description": "description", "price" : 0})
    assert response.status_code == 200
    assert response.json() == {"name" : "test", "description": "description", "price" : 0}

def test_update_not_inventory_item():
    response = client.put("/update-item/3", json = {"name" : "test", "description": "description", "price" : 0}) # Puedo poner -1?
    assert response.status_code == 404
    assert response.json() == {"detail" : "Item ID does not exists."}

### Delete tests    

def test_delete_item():
    response = client.delete("/delete-item?item_id=0")
    assert response.status_code == 200
    assert response.json() == {"Success" : "Item deleted"}

def test_delete_not_inventory_item():
    response = client.delete("delete-item?item_id=4")
    assert response.status_code == 404
    assert response.json() == {"detail" : "Item ID does not exists."}
