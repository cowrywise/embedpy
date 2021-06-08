import json
import uuid
from embed.common import APIResponse


class Wallet(APIResponse):
    """
    Handles all queries for Wallet
    """

    def __init__(self, api_session):
        super(Wallet, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_wallets(self):
        method = "GET"
        url = self.base_url + "wallets"
        return self.get_essential_details(method, url)

    def get_wallet(self, wallet_id):
        method = "GET"
        url = self.base_url + f"wallets/{wallet_id}"
        return self.get_essential_details(method, url)

    def create_wallet(self, account_id, currency="NGN", idempotency_key=None):
        method = "POST"
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
        url = self.base_url + "wallets"
        payload = json.dumps({"account_id": account_id, "currency_code": currency})
        return self.get_essential_details(method, url, payload)
