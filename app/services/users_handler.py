from ast import Str
from http import HTTPStatus
import json
from json.decoder import JSONDecodeError
from ..exception import ValidateDataJsonError
import os

DATABASE = os.getenv("DATABASE")

def read_json(file_path: str):
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    except JSONDecodeError:
        return []
    except FileNotFoundError:
        os.system(f"touch {DATABASE}")
        return []

def write_json(file_path: str, data: dict):
    json_list = read_json(file_path)
    json_list.append(data)

    with open(file_path, 'w') as json_file:
        json.dump(json_list, json_file, indent=2)
        return data

def validate_email(email: str):
    data_base = read_json(DATABASE)

    return [emails for emails in data_base if emails["email"] == email]

def validate_json_data_email(email, nome):
    if type(email) != str or type(nome) != str:
        return ValidateDataJsonError
    else:
        return False


def add_id_users():
    data_base = read_json(DATABASE)

    if data_base:
        list_id = []
        for i in data_base:
            list_id.append(i["id"])

        last_id = list_id[-1] + 1
        return last_id

    return 1


def verify_str_email(is_string: str):
    if type(is_string) == str:
        return is_string.lower()
    
    return is_string

def verify_str_nome(is_string: str):
    if type(is_string) == str:
        return is_string.title()
    
    return is_string

