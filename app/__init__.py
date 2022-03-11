from http import HTTPStatus
import os
from flask import Flask, request
from flask import jsonify
from .services import read_json
from .services import write_json
from .models import User
from .exception import ValidateEmailError
from .exception import ValidateDataJsonError

app = Flask(__name__)

teste = os.getenv("DATABASE")

@app.get("/user")
def get_users():
    return {"data": User.get_users()}, HTTPStatus.OK


@app.post("/user")
def post_user():
    data = request.get_json()
    user = User(**data)

    try:
        return user.created_users(), HTTPStatus.CREATED
    except ValidateEmailError:
        return { "error": "User already exists."}, HTTPStatus.CONFLICT
    except ValidateDataJsonError as e:
        # return {"wrong fields": [{}, {}]}, e.status_code
        return {"wrong fields": e.message}, e.status_code


