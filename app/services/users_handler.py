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

def validate_json_data_email(value):
    if type(value) != str:
        return ValidateDataJsonError
    else:
        return value
