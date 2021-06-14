from requests import ConnectionError, RequestException


class EmbedError(Exception):
    pass


class CredentialsError(EmbedError):
    pass


class ValidationError(EmbedError):
    pass


class ServerError(EmbedError):
    pass


class EmbedConnectionError(ConnectionError, RequestException):
    pass


def show_details(_):
    print(f"{_.args[0]} was not found in the environment variables")
    raise
