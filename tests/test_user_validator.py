from utils.user_validator import UserValidator

validator = UserValidator(None) 


# ------------------------------
# Document
# ------------------------------
def test_valid_document():
    assert validator.is_valid_document("123")
    assert validator.is_valid_document("000456")
    assert validator.is_valid_document("987654321")

def test_invalid_document():
    assert not validator.is_valid_document("12a34")
    assert not validator.is_valid_document(" ")
    assert not validator.is_valid_document("")
    assert not validator.is_valid_document("123 456")


# ------------------------------
# Type Document
# ------------------------------
def test_valid_type_document():
    assert validator.is_valid_type_document("CC")
    assert validator.is_valid_type_document("TI")
    assert validator.is_valid_type_document("NIT")

def test_invalid_type_document():
    assert not validator.is_valid_type_document("cc") 
    assert not validator.is_valid_type_document("DNI")
    assert not validator.is_valid_type_document("")
    assert not validator.is_valid_type_document("123")


# ------------------------------
# Name
# ------------------------------
def test_valid_name():
    assert validator.is_valid_name("Juan")
    assert validator.is_valid_name("Maria")

def test_invalid_name():
    assert not validator.is_valid_name("Juan1")
    assert not validator.is_valid_name("Juan!")
    assert not validator.is_valid_name("Juan Pérez") 
    assert not validator.is_valid_name("")


# ------------------------------
# Last Name
# ------------------------------
def test_valid_last_name():
    assert validator.is_valid_last_name("Gomez")
    assert validator.is_valid_last_name("Lopez")

def test_invalid_last_name():
    assert not validator.is_valid_last_name("123")
    assert not validator.is_valid_last_name("Gómez!")
    assert not validator.is_valid_last_name("Ana María") 
    assert not validator.is_valid_last_name("")


# ------------------------------
# Email
# ------------------------------
def test_valid_email():
    assert validator.is_valid_email("test@example.com")
    assert validator.is_valid_email("user.name@mail.co")
    assert validator.is_valid_email("test_123@domain.net")

def test_invalid_email():
    assert not validator.is_valid_email("test@")
    assert not validator.is_valid_email("user@.com")
    assert not validator.is_valid_email("user@com")
    assert not validator.is_valid_email("user.com")
    assert not validator.is_valid_email("")


# ------------------------------
# Password
# ------------------------------
def test_valid_password():
    assert validator.is_valid_password("Hola123@")
    assert validator.is_valid_password("ClaveSegura1!")
    assert validator.is_valid_password("XyZ$7890")

def test_invalid_password():
    assert not validator.is_valid_password("hola123")       
    assert not validator.is_valid_password("HOLA123!")      
    assert not validator.is_valid_password("Hola!")        
    assert not validator.is_valid_password("Hola123456")    
    assert not validator.is_valid_password("")


# ------------------------------
# Re password
# ------------------------------
def test_valid_re_password():
    assert validator.is_valid_re_password("Hola123@", "Hola123@")
    assert validator.is_valid_re_password("ClaveSegura1!", "ClaveSegura1!")
    assert validator.is_valid_re_password("XyZ$7890", "XyZ$7890")

def test_invalid_password():
    assert not validator.is_valid_re_password("Hola123@", "dwadafaw")
    assert not validator.is_valid_re_password("ClaveSegura1!", "dawgqwa")
    assert not validator.is_valid_re_password("XyZ$7890", "fqwasw")
    
    
# ------------------------------
# Years
# ------------------------------
def test_valid_years():
    assert validator.is_valid_years("5")
    assert validator.is_valid_years("25")
    assert validator.is_valid_years("120")
    assert validator.is_valid_years("999")

def test_invalid_years():
    assert not validator.is_valid_years("1000")    
    assert not validator.is_valid_years("abc")      
    assert not validator.is_valid_years("")        
    assert not validator.is_valid_years("12a")  
     