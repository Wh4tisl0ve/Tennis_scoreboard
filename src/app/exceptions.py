class UserError(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.__code = code

    @property
    def code(self) -> int:
        return self.__code

    @property
    def message(self) -> int:
        return self.args[0]


class NotFoundError(UserError):
    def __init__(self, message: str):
        super().__init__(message, 404)


class InvalidFieldError(UserError):
    def __init__(self, message: str):
        super().__init__(message, 400)
