import re

class UserValidator:
    def __init__(self, db):
        self.db = db
        
    # Document
    def is_valid_document(self, document):
        pattern = r"^[0-9]+$"
        return re.match(pattern, document) is not None
    
    def is_document_registered(self, document):
        existing_users = self.db.collection("users").where("document", "==", document).stream()
        return any(existing_users)
    
    
    # Type Document
    def is_valid_type_document(self, type_document):
        valid_types = {
        "CC", 
        "TI", 
        "CE",  
        "PA", 
        "RC",  
        "NUIP", 
        "PEP",  
        "PPT",  
        "NIT"
        }
        return type_document in valid_types
    
    
    # Name
    def is_valid_name(self, name):
        pattern = r"^[a-zA-Z]+$"
        return re.match(pattern, name) is not None
    
    
    # Last Name
    def is_valid_last_name(self, last_name):
        pattern = r"^[a-zA-Z]+$"
        return re.match(pattern, last_name) is not None
    
    
    # Email
    def is_valid_email(self, email):
        pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None
    
    def is_email_registered(self, email):
        existing_users = self.db.collection("users").where("email", "==", email).stream()
        return any(existing_users)
    
    
    # Password
    def is_valid_password(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$"
        return re.match(pattern, password) is not None
    
    
    # Re password
    def is_valid_re_password(self, password, re_password):
        return password == re_password
    
    
    # Years
    def is_valid_years(self, years):
        pattern = r"^[0-9]{1,3}$"
        return re.match(pattern, years) is not None
    