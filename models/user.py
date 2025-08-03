class User:
    def __init__(self, document: int, document_type: str, name: str, last_names: str, email: str, password: str, re_password: str, years: int):
        self.document = document
        self.document_type = document_type
        self.name = name
        self.last_names = last_names
        self.email = email
        self.password = password
        self.re_password = re_password
        self.years = years
        
        
    def to_dict(self):
        """
        Returns the user data as a dictionary for database insertion
        (excluding re_password for security
        """
        return {
            'document': self.document, 
            'document_type': self.document_type,
            'name': self.name,
            'last_names': self.last_names,
            'email': self.email,
            'password': self.password,
            'years': self.years
        }
        