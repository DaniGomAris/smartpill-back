from flask import Blueprint, request, jsonify
from firebase_config import db
from utils.user_validator import UserValidator
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint("users", __name__)
validator = UserValidator(db)

# Obtain all users
@user_bp.route("/", methods = ["GET"])
#@jwt_required()
def get_users():
    collection = db.collection("users")
    documents = collection.stream()
    users = []
    
    for doc in documents:
        user_data = doc.to_dict()
        user_data["id"] = doc.id
        users.append(user_data)
    
    return jsonify(users)

# Register user 
@user_bp.route("/", methods = ["POST"])
def add_user():
    data = request.get_json()
    
    # Obtain user data
    document = data.get("document")
    document_type = data.get("document_type")
    name = data.get("name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")
    re_password = data.get("re_password")
    years = data.get("years")
    
    # Format validations
    format_errors = {}
    
    if not validator.is_valid_document(document):
        format_errors["document"] = "Invalid document format"
    
    if not validator.is_valid_document_type(document_type):
        format_errors["document_type"] = "Invalid document_type format"
        
    if not validator.is_valid_name(name):
        format_errors["name"] = "Invalid name format"
        
    if not validator.is_valid_last_name(last_name):
        format_errors["last_name"] = "Invalid last_name format"
    
    if not validator.is_valid_email(email):
        format_errors["email"] = "Invalid email format"
    
    if not validator.is_valid_password(password):
        format_errors["password"] = "Invalid password format"
    
    if not validator.is_valid_re_password(password, re_password):
        format_errors["re_password"] = "Passwords do not match"
        
    if not validator.is_valid_years(years):
        format_errors["years"] = "Invalid years format"
        
    if format_errors:
        return jsonify({"error": format_errors}), 400
    

    # Conflict validations 
    conflict_errors = {}
    
    if validator.is_document_registered(document):
        conflict_errors["document"] = "Document already registered"
        
    if validator.is_email_registered(email):
        conflict_errors["email"] = "Email already registered"
        
    if conflict_errors:
        return jsonify({"error": conflict_errors}), 409
    
    # Hash password and clean data
    data["password"] = generate_password_hash(password)
    data.pop("re_password", None)
    
    # Save to Firestore
    ref = db.collection("users").add(data)[1]
    return jsonify({"message": "User added", "id": ref.id}), 201


# Delete user
@user_bp.route("/<user_id>", methods = ["DELETE"])
@jwt_required()
def delete_user(user_id):
    try:
        db.collection("users").document(user_id).delete()
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# Update user
@user_bp.route("/<user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    try:
        db.collection("users").document(user_id).update(data)
        return jsonify({"message": "User updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Login with token generation
@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    try:
        users = db.collection("users").where("email", "==", email).stream()
        user = next(users, None)

        if user is None:
            return jsonify({"error": "User not found"}), 404

        user_data = user.to_dict()
        if not check_password_hash(user_data["password"], password):
            return jsonify({"error": "Invalid password"}), 401

        # Create token with ID
        access_token = create_access_token(identity=user.id)

        # Dont send a password
        user_data.pop("password", None)

        return jsonify({
            "access_token": access_token,
            "user": {**user_data, "id": user.id}
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Obtain data to logged user
@user_bp.route("/me", methods=["GET"])
@jwt_required()
def get_logged_user():
    user_id = get_jwt_identity()
    try:
        user_doc = db.collection("users").document(user_id).get()
        if not user_doc.exists:
            return jsonify({"error": "User not found"}), 404
        
        user_data = user_doc.to_dict()
        user_data.pop("password", None)
        return jsonify({**user_data, "id": user_doc.id}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500 
    