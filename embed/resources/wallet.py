import json
from embed.common import APIResponse


class Wallet(APIResponse):
    """
    Handles all queries for Wallet
    """

    def __init__(self, api_host, token, version):
        super(Wallet, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_wallets(self):
        method = "GET"
        url = self.api_host + "wallets"
        return self.get_essential_details(method, url)

    def get_wallet(self, wallet_id):
        method = "GET"
        url = self.api_host + f"wallets/{wallet_id}"
        return self.get_essential_details(method, url)

    def create_wallet(self, account_id, currency="NGN"):
        method = "POST"
        url = self.api_host + "wallets"
        payload = json.dumps({"account_id": account_id, "currency_code": currency})
        return self.get_essential_details(method, url, payload)

    def transfer_from_wallet(self, account_id, amount, product_code):
        method = "POST"
        url = self.api_host + f"wallets/{account_id}/transfer"
        payload = json.dumps({"amount": amount, "product_code": product_code})
        return self.get_essential_details(method, url, payload)
