import os
from embed.errors import APICredentialsError
from embed.accounts import Account
from embed.token import Token


class APIClient(object):
    """
    Initiates connection to the API
    """

    SANDBOX_BASE_API_URI = 'https://sandbox.cowrywise.com'
    API_VERSION = "v1"
    TIMEOUT = 40

    def __init__(self, client_id=None, client_secret=None, base_url=None, api_version=None, timeout=None):

        if None in (client_id, os.environ.get("CLIENT_ID")):
            raise APICredentialsError("Provide client ID or set in environment variable.")
        if None in (client_secret or os.environ.GET('CLIENT_SECRET')):
            raise APICredentialsError("Provide client secret or set in environment variable.")

        self.client_id = client_id
        self.client_secret = client_secret
        self.api_version = api_version or self.API_VERSION
        self.base_url = base_url or self.SANDBOX_BASE_API_URI
        self.timeout = timeout or self.TIMEOUT

    @property
    def access_token(self):
        access_token, _ = Token(self.client_id, self.client_secret, self.base_url).get_access_token()
        return access_token

    @property
    def accounts(self):
        return Account(self.base_url, self.access_token, self.api_version)