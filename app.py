from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from routes.user_route import user_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)
