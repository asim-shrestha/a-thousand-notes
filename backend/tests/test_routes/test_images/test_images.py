import io
from tests import client

IMAGE_ROUTE = '/image'

def test_get_non_existant_image():
    non_existant_id = 999
    response = client.get(f"{IMAGE_ROUTE}/{non_existant_id}")

    assert response.status_code == 404

