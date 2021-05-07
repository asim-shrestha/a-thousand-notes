import io
from pathlib import Path
from tests import client

IMAGE_ROUTE = '/image'

def test_get_non_existant_image():
    non_existant_id = 999
    response = client.get(f"{IMAGE_ROUTE}/{non_existant_id}")

    assert response.status_code == 404

def test_cannot_upload_non_image(text_file):
    response = client.post(f"{IMAGE_ROUTE}/", files={
        "files": text_file
        })
    assert response.status_code == 400

def test_image_upload_succeeds(image_file):
    response = client.post(f"{IMAGE_ROUTE}/", files={
        "files": image_file
        })
    assert response.status_code == 200

def test_multi_non_image_upload_fails(text_file):
    response = client.post(f"{IMAGE_ROUTE}/", files=[
        ("files", text_file),
        ("files", text_file),
        ("files", text_file),
    ])
#     assert response.status_code == 400

def test_multi_upload_fails_with_one_non_image(text_file, image_file):
    response = client.post(f"{IMAGE_ROUTE}/", files=[
        ("files", image_file),
        ("files", text_file),
    ])
    assert response.status_code == 400

def test_multi_image_upload_succeeds(text_file, image_file):
    response = client.post(f"{IMAGE_ROUTE}/", files=[
        ("files", image_file),
        ("files", image_file),
    ])
    assert response.status_code == 400