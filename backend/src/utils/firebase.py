from hashlib import new
import pyrebase
from fastapi import UploadFile
import uuid
import os
import shutil

firebaseConfig = {
    "apiKey": os.environ.get("FIREBASE_API_KEY"),
    "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
    "databaseURL": os.environ.get("FIREBASE_DATABASE_URL"),
    "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.environ.get("FIREBASE_APP_ID"),
    "measurementId": os.environ.get("FIREBASE_MEASUREMENT_ID")
  };

firebase_app = pyrebase.initialize_app(firebaseConfig)
storage = firebase_app.storage()
FIREBASE_IMAGES_PATH = "images"

def upload_to_firebase(file: UploadFile) -> dict:
    # Generate id for file
    file_id = str(uuid.uuid4())
    firebase_url = f"{FIREBASE_IMAGES_PATH}/{file_id}"

    # Upload local version to firebase
    storage.child(firebase_url).put(file)

    # Return the firebase url
    return {
        "url": firebase_url,
        "full_url": storage.child(firebase_url).get_url(None)
    }

def remove_from_firebase(url: str):
        # Upload local version to firebase
    storage.child(url).delete()

def get_firebase_url(url):
    return url