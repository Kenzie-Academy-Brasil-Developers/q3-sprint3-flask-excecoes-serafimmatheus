class ValidateEmailError(Exception):
    ...


class ValidateDataJsonError(Exception):
    def __init__(self, message=None, status_code=400, email="not informed"):
        if message:
            self.message = message
        else:
            
            self.message = f"teste {type(email)}"

        self.status_code = status_code