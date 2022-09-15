
class JokeValidationException(Exception):
    def __init__(self, message, model, error_code):
        super().__init__(message)
        self.message = message
        self.model = model
        self.error_code = error_code
