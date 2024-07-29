import sys
import os
from fastapi.testclient import TestClient
from main import app
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))
client = TestClient(app)
def test_get_name():
    response = client.get("/name")
    assert response.status_code == 200
    assert response.json() == "this is my name"
