from tests import client

IMAGE_ROUTE = '/image'
IMAGE_NAME = 'Im a new image!'


def test_get_non_existant_image():
    non_existant_id = 999
    response = client.get(f"{IMAGE_ROUTE}/{non_existant_id}")

    assert response.status_code == 404


def test_cannot_upload_non_image(text_file):
    response = client.post(f"{IMAGE_ROUTE}/name/{IMAGE_NAME}", files={
        "files": text_file
        })
    assert response.status_code == 400


def test_image_upload_succeeds(image_file):
    response = client.post(f"{IMAGE_ROUTE}/name/{IMAGE_NAME}", files={
        "files": image_file
        })

    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id']
    assert data[0]['image_url']
    assert data[0]['spotify_name']
    assert data[0]['spotify_uri']
    assert data[0]['spotify_preview_url']


def test_multi_non_image_upload_fails(text_file):
    response = client.post(f"{IMAGE_ROUTE}/name/{IMAGE_NAME}", files=[
        ("files", text_file),
        ("files", text_file),
        ("files", text_file),
    ])
    assert response.status_code == 400


def test_multi_upload_fails_with_one_non_image(text_file, image_file):
    response = client.post(f"{IMAGE_ROUTE}/name/{IMAGE_NAME}", files=[
        ("files", image_file),
        ("files", text_file),
    ])
    assert response.status_code == 400


def test_cannot_delete_non_existant_image():
    non_existant_id = 967
    response = client.delete(f"{IMAGE_ROUTE}/{non_existant_id}")
    assert response.status_code == 404


def test_create_get_delete(image_file):
    response = client.post(f"{IMAGE_ROUTE}/name/{IMAGE_NAME}", files={
        "files": image_file
    })

    assert response.status_code == 200
    id = response.json()[0]['id']

    response = client.get(f"{IMAGE_ROUTE}/{id}")
    assert response.status_code == 200

    response = client.delete(f"{IMAGE_ROUTE}/{id}")
    assert response.status_code == 200

    response = client.get(f"{IMAGE_ROUTE}/{id}")
    assert response.status_code == 404


def test_get_all_images_with_no_images():
    response = client.get(f"{IMAGE_ROUTE}/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_all_images_with_image(image_file):
    client.post(f"{IMAGE_ROUTE}/name/{IMAGE_NAME}", files={
        "files": image_file
    })

    response = client.get(f"{IMAGE_ROUTE}/")
    assert response.status_code == 200
    assert len(response.json()) == 1