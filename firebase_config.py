import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

key_path = os.getenv("FIREBASE_KEY_PATH")
credentials = credentials.Certificate(key_path)
firebase_admin.initialize_app(credentials)

db = firestore.client()
