import json
from app import create_app

app = create_app()
client = app.test_client()

def test_multiply_success():
    response = client.post("/multiply", json={"a": 6, "b": 7})
    assert response.status_code == 200
    assert response.get_json()["result"] == 42
