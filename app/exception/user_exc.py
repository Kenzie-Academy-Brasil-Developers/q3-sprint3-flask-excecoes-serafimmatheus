class ValidateEmailError(Exception):
    ...


class ValidateDataJsonError(Exception):
    def __init__(self, message=None, status_code=400, email="not informed", name="not informed"):
        if message:
            self.message = message
        else:
            nameFormated = {"name": type(name)}
            emailFormated = {"email": type(email)}
           
            # self.message = [nameFormated, emailFormated]
            self.message = [f'{nameFormated}', f'{emailFormated}']

        self.status_code = status_code