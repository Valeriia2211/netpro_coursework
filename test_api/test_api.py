import base64
from app.rest_api import create_app

def auth_header():
    token = base64.b64encode(b"admin:1234").decode("utf-8")
    return {"Authorization": f"Basic {token}"}

def get_client():
    app = create_app()
    return app.test_client()

def test_get_items():
    client = get_client()
    response = client.get("/items", headers=auth_header())
    assert response.status_code == 200

def test_get_single_item():
    client = get_client()
    response = client.get("/items/1", headers=auth_header())
    assert response.status_code == 200

def test_create_item():
    client = get_client()
    new_item = {"name": "Tablet", "price": 300, "color": "gray"}
    response = client.post("/items", json=new_item, headers=auth_header())
    assert response.status_code == 200
