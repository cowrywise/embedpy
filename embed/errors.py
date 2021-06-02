from requests import ConnectionError, RequestException


class Error(RequestException):
    pass


class APIError(Error):
    pass


class APICredentialsError(Error):
    pass


class APIConnectionError(Error, ConnectionError):
    pass


class ValidationError(Error):
    pass


def show_details(_):
    print(f"{_.args[0]} was not found in the environment variables")
    raise
