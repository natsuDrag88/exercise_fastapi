import base64

from fastapi.testclient import TestClient
from sqlalchemy.util import b64encode

from app_fastapi.main import app

client = TestClient(app)


def test_get_all_empleados_without_authentication():
    result_response_messaje = {"detail":"Not authenticated"}
    response = client.get('/empleados')
    assert response.status_code == 401
    assert result_response_messaje == response.json()


def test_get_all_empleados_with_authentication():
    headers = {
        'Authorization': 'Basic NWEyNWM5ZjI1YzMzNGY0MTk3ZGY0ZDJhYWZjYTVmZDk6MTIz'
    }
    response = client.get('/empleados/', headers=headers)
    assert response.status_code == 401
