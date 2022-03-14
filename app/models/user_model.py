from app.services import read_json
from app.services import write_json
from app.services import validate_email
from app.services import validate_json_data_email
from app.services import add_id_users
from app.services import verify_str_nome
from app.services import verify_str_email
from ..exception import ValidateEmailError
from ..exception import ValidateDataJsonError
import os

DATABASE_FILE = os.getenv("DATABASE")

class User():

    def __init__(self, nome:str, email: str):
        
        self.nome = verify_str_nome(nome)
        self.email = verify_str_email(email)  
            
        self.id = add_id_users()


    @staticmethod
    def get_users():
        return read_json(DATABASE_FILE)


    def created_users(self):

        if validate_email(self.email):
            raise ValidateEmailError

        if validate_json_data_email(self.email, self.nome):
            raise ValidateDataJsonError(email=self.email, nome=self.nome)

        return write_json(DATABASE_FILE, self.__dict__)