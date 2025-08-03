import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# Cargar JSON desde variable de entorno
firebase_key_str = os.getenv("FIREBASE_KEY")

# Convertir a dict
firebase_key_dict = json.loads(firebase_key_str)

# Inicializar credenciales
cred = credentials.Certificate(firebase_key_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()
