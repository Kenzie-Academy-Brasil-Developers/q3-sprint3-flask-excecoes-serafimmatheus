class ValidateEmailError(Exception):
    ...


class ValidateDataJsonError(Exception):
    def __init__(self, message=None, status_code=400, email="not informed", nome="not informed"):
        if message:
            self.message = message
        else:
            nameFormated = {"nome": type(nome).__name__}
            emailFormated = {"email": type(email).__name__}
           
            self.message = [nameFormated, emailFormated]
            # self.message = [f'{nameFormated}', f'{emailFormated}']

        self.status_code = status_code