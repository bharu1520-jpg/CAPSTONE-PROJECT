import requests

BASE_URL = "http://localhost:5000"


def test_health():
    r = requests.get(f"{BASE_URL}/health")
    assert r.status_code == 200


def test_users():
    r = requests.get(f"{BASE_URL}/users")
    assert r.status_code == 200
