import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables from .env file
load_dotenv()

# Get the key path from the environment variable
key_path = os.getenv("FIREBASE_KEY_PATH")

# Initialize Firebase with the service account key
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()
print("Firestore connection successful:", db)
