import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust import based on your application structure

client = TestClient(app)

def test_get_name():
    response = client.get("/name")
    assert response.status_code == 200
    assert response.json() == "this is my name"
