from utils import is_valid_email
from dbhelpers import getuser,insert_user
from models import User

def login(email, password):
    if not is_valid_email(email):
        print("invalid email")
        return None

    user = getuser(email, password)
    return user


def register(fname, lname, email, password, confirm_pass, phone):
    if not is_valid_email(email):
        print("invalid email")
        return False
    if not (password and confirm_pass and password == confirm_pass):
        print("incompatible password")
        return False
    new_user = User(fname, lname, email, password, phone)
    return insert_user(new_user)