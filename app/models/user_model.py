from app.services import read_json
from app.services import write_json
from app.services import validate_email
from app.services import validate_json_data_email
from ..exception import ValidateEmailError
from ..exception import ValidateDataJsonError
import os

DATABASE_FILE = os.getenv("DATABASE")

class User():

    def __init__(self, name:str, email: str):
        self.name = name
        self.email = email


    @staticmethod
    def get_users():
        return read_json(DATABASE_FILE)


    def created_users(self):

        if validate_email(self.email):
            raise ValidateEmailError

        if validate_json_data_email(self.email):
            raise ValidateDataJsonError(email=self.email)

        return write_json(DATABASE_FILE, self.__dict__)