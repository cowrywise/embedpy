import os

from embed.errors import APICredentialsError
from embed.resources.account import Account
from embed.resources.asset import Asset
from embed.resources.index import Index
from embed.resources.investment import Investment
from embed.resources.price import Price
from embed.resources.saving import Saving
from embed.resources.token import Token
from embed.resources.trade import Trade
from embed.resources.transaction import Transaction
from embed.resources.wallet import Wallet


class Client(object):
    """
    This is the main entry point to the Cowrywise
    Embed API.

    An instance of this class gives direct access to all
    the resources exposed by this api.

    Full API docs available at https://developers.cowrywise.com
    """

    BASE_API_URI = "https://sandbox.cowrywise.com"
    API_VERSION = "v1"
    TIMEOUT = 40

    def __init__(
            self,
            client_id=None,
            client_secret=None,
            base_url=None,
            api_version=None,
    ):

        self.client_id = client_id or os.getenv("CLIENT_ID")
        if self.client_id is None:
            raise APICredentialsError(
                "Please provide client ID or set CLIENT_ID in environment variable."
            )

        self.client_secret = client_secret or os.getenv("CLIENT_SECRET")
        if self.client_secret is None:
            raise APICredentialsError(
                "Provide client secret or set CLIENT_SECRET in environment variable."
            )

        self.api_version = api_version or self.API_VERSION
        self.base_url = base_url or self.BASE_API_URI

        self._access_token, _ = Token(self.client_id, self.client_secret, self.base_url).get_access_token()
        self._accounts = Account(self.base_url, self.access_token, self.api_version)
        self._assets = Asset(self.base_url, self.access_token, self.api_version)
        self._investments = Investment(self.base_url, self.access_token, self.api_version)
        self._indexes = Index(self.base_url, self.access_token, self.api_version)
        self._savings = Saving(self.base_url, self.access_token, self.api_version)
        self._trades = Trade(self.base_url, self.access_token, self.api_version)
        self._transactions = Transaction(self.base_url, self.access_token, self.api_version)
        self._prices = Price(self.base_url, self.access_token, self.api_version)
        self._wallets = Wallet(self.base_url, self.access_token, self.api_version)

    @property
    def access_token(self):
        return self._access_token

    @property
    def Accounts(self):
        return self._accounts

    @property
    def Assets(self):
        return self._assets

    @property
    def Investments(self):
        return self._investments

    @property
    def Indexes(self):
        return self._indexes

    @property
    def Savings(self):
        return self._savings

    @property
    def Trades(self):
        return self._trades

    @property
    def Transactions(self):
        return self._transactions

    @property
    def Prices(self):
        return self._prices

    @property
    def Wallets(self):
        return self._wallets
