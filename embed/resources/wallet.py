import json
from embed.common import APIResponse


class Wallet(APIResponse):
    """
    Handles all queries for Wallet
    """

    def __init__(self, api_session):
        super(Wallet, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_wallets(self, **kwargs):
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "wallets"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_wallet(self, wallet_id):
        method = "GET"
        url = self.base_url + f"wallets/{wallet_id}"
        return self.get_essential_details(method, url)

    def create_wallet(self, **kwargs):

        required = ["account_id", "currency_code"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "wallets"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def transfer(self, **kwargs):
        required = ["wallet_id", "product_code", "amount"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        wallet_id = kwargs.pop("wallet_id")
        method = "POST"
        url = self.base_url + f"wallets/{wallet_id}/transfer"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
