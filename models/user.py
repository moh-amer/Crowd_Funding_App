import os.path
import uuid
class User:
    file_name = "user.db"
    def __init__(self, firstname, lastname, email, password, phone=''):
        self.id = str(uuid.uuid1())
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = phone

    def setID(self, id):
        self.id = id

    def __str__(self):
        output = ":".join(self.__dict__.values())
        return str(output)