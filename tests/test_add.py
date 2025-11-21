import json
from app import create_app

app = create_app()
client = app.test_client()

def test_add_success():
    response = client.post("/add", json={"a": 10, "b": 20})
    assert response.status_code == 200
    assert response.get_json()["result"] == 30

