import os
import shutil
from pathlib import Path

import pytest

MOCK_DATA_DIR = Path(__file__).parent / 'mock_data'
TEXT_FILE_NAME = 'file.txt'
IMAGE_FILE_NAME = 'file.jpg'


@pytest.fixture()
def text_file():
    assert (file_dir := MOCK_DATA_DIR / TEXT_FILE_NAME).exists()
    with open(str(file_dir), "r+") as text_file:
        yield text_file


@pytest.fixture()
def image_file():
    assert (file_dir := MOCK_DATA_DIR / IMAGE_FILE_NAME).exists()
    with open(str(file_dir), "rb") as image_file:
        yield image_file
