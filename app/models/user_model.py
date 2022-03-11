from app.services import read_json
from app.services import write_json
from app.services import validate_email
from app.services import validate_json_data_email
from app.services import add_id_users
from ..exception import ValidateEmailError
from ..exception import ValidateDataJsonError
import os

DATABASE_FILE = os.getenv("DATABASE")

class User():

    def __init__(self, name:str, email: str):
        self.name = name
        self.email = email

        if self.name == str and self.email == str:
            self.name = name.title()
            self.email = email.lower()
            
        self.id = add_id_users()


    @staticmethod
    def get_users():
        return read_json(DATABASE_FILE)


    def created_users(self):

        if validate_email(self.email):
            raise ValidateEmailError

        if validate_json_data_email(self.email, self.name):
            raise ValidateDataJsonError(email=self.email, name=self.name)

        return write_json(DATABASE_FILE, self.__dict__)