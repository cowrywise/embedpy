import os

from embed.errors import CredentialsError
from embed.resources.account import Account
from embed.resources.asset import Asset
from embed.resources.index import Index
from embed.resources.investment import Investment
from embed.resources.price import Price
from embed.resources.saving import Saving
from embed.resources.trade import Trade
from embed.resources.transaction import Transaction
from embed.resources.wallet import Wallet
from embed.common import APISession


class Client(object):
    """
    This is the main entry point to the Cowrywise
    Embed API.

    An instance of this class gives direct access to all
    the resources exposed by this api.

    Full API docs available at https://developers.cowrywise.com
    """

    BASE_API_URI = "https://sandbox.embed.cowrywise.com"
    API_VERSION = "v1"
    TIMEOUT = 40

    def __init__(
        self,
        client_id=None,
        client_secret=None,
        base_url=None,
        api_version=None,
    ):

        self._client_id = client_id or os.getenv("CLIENT_ID")
        if self._client_id is None:
            raise CredentialsError(
                "Provide client id or set CLIENT_ID as environment variable."
            )

        self._client_secret = client_secret or os.getenv("CLIENT_SECRET")
        if self._client_secret is None:
            raise CredentialsError(
                "Provide client secret or set CLIENT_SECRET in environment variable."
            )

        self._api_version = api_version or self.API_VERSION
        self._base_url = base_url or self.BASE_API_URI

        self._session = APISession(
            self._base_url, self._client_id, self._client_secret, self._api_version
        )

        self._accounts = Account(self._session)
        self._assets = Asset(self._session)
        self._investments = Investment(self._session)
        self._indexes = Index(self._session)
        self._savings = Saving(self._session)
        self._trades = Trade(self._session)
        self._transactions = Transaction(self._session)
        self._prices = Price(self._session)
        self._wallets = Wallet(self._session)

    @property
    def access_token(self):
        return self._session.token

    @property
    def accounts(self):
        return self._accounts

    @property
    def assets(self):
        return self._assets

    @property
    def investments(self):
        return self._investments

    @property
    def indexes(self):
        return self._indexes

    @property
    def savings(self):
        return self._savings

    @property
    def trades(self):
        return self._trades

    @property
    def transactions(self):
        return self._transactions

    @property
    def prices(self):
        return self._prices

    @property
    def wallets(self):
        return self._wallets
