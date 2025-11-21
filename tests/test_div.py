import json
from app import create_app

app = create_app()
client = app.test_client()

def test_divide_success():
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.get_json()["result"] == 5

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
