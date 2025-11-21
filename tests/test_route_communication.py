import json
from app import create_app

app = create_app()
client = app.test_client()

def test_route1_calls_route2_multiply():
    response = client.get("/route1-call-multiply")
    assert response.status_code == 200
    assert response.get_json()["multiply_result"] == 30

def test_route1_calls_route2_add():
    response = client.get("/route1-call-add")
    assert response.status_code == 200
    assert response.get_json()["add_result"] == 7

def test_route2_calls_route1():
    response = client.get("/route2-call-add")
    assert response.status_code == 200
    assert response.get_json()["add_result"] == 25   # 10+15 from internal route1
