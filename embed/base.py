import os
from embed.errors import APICredentialsError
from embed.resources.account import Account
from embed.resources.asset import Asset
from embed.resources.investment import Investment
from embed.resources.index import Index
from embed.resources.saving import Saving
from embed.resources.token import Token


class APIClient(object):
    """
    This is the main entry point to the Cowrywise
    Embed API.

    An instance of this class gives direct access to all
    the resources exposed by this api.

    Full API docs available at https://developers.cowrywise.com
    """

    BASE_API_URI = 'https://sandbox.cowrywise.com'
    API_VERSION = "v1"
    TIMEOUT = 40

    def __init__(self, client_id=None, client_secret=None, base_url=None, api_version=None, timeout=None):

        self.client_id = client_id or os.getenv("CLIENT_ID")
        if self.client_id is None:
            raise APICredentialsError("Please provide client ID or set in environment variable.")

        self.client_secret = client_secret or os.getenv('CLIENT_SECRET')
        if self.client_secret is None:
            raise APICredentialsError("Provide client secret or set in environment variable.")

        self.api_version = api_version or self.API_VERSION
        self.base_url = base_url or self.BASE_API_URI
        self.timeout = timeout or self.TIMEOUT

    @property
    def access_token(self):
        access_token, _ = Token(self.client_id, self.client_secret, self.base_url).get_access_token()
        return access_token

    @property
    def accounts(self):
        return Account(self.base_url, self.access_token, self.api_version)

    @property
    def assets(self):
        return Asset(self.base_url, self.access_token, self.api_version)

    @property
    def investments(self):
        return Investment(self.base_url, self.access_token, self.api_version)

    @property
    def indexes(self):
        return Index(self.base_url, self.access_token, self.api_version)

    @property
    def savings(self):
        return Saving(self.base_url, self.access_token, self.api_version)