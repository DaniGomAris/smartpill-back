import firebase_admin
from firebase_admin import credentials, firestore

# Ruta correcta al secret file en Render
firebase_key_path = "/etc/secrets/firebase_key.json"

# Inicializar Firebase con el archivo secreto
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred)

# Inicializar Firestore
db = firestore.client()
