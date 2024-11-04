
class AuthenticationError(Exception):
    def __init__(self, message: str = "Unauthorized"):
        self.message = message

class AuthorizationError(Exception):
    def __init__(self, message: str = "Forbidden"):
        self.message = message
