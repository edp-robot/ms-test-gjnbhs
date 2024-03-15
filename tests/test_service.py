import requests

def test_root_call():
    r = requests.get('http://localhost:8080/api/hello')
    assert r.status_code == 200


def test_root_call_2():
    r = requests.get('http://localhost:8080/api/hello')
    assert r.status_code != 404