import os
import sys
from fastapi.testclient import TestClient

# Adjust the import path to include the actions/src directory
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'src')))

from main import app

client = TestClient(app)

def test_get_name():
    response = client.get("/name")
    assert response.status_code == 200
    assert response.json() == "this is my name the mohan who are you yo fucker"
