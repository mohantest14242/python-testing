import sys
import os

# Add the directory containing `src` to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from src.main import app  # Import the FastAPI application

from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_name():
    response = client.get("/name")
    assert response.status_code == 200
    assert response.json() == "this is my name"
