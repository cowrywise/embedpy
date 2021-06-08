import json
import uuid
from embed.common import APIResponse


class Transfer(APIResponse):
    """
    Handles all queries for Wallet
    """

    def __init__(self, api_session):
        super(Transfer, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_transfers(self):
        method = "GET"
        url = self.base_url + "transfers"
        return self.get_essential_details(method, url)

    def get_transfer(self, transfer_id):
        method = "GET"
        url = self.base_url + f"transfers/{transfer_id}"
        return self.get_essential_details(method, url)

    def initiate_transfer(self, source_wallet_id, destination_product_code,
                          amount, currency_code, idempotency_key=None):
        method = "POST"
        url = self.base_url + "transfers"
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
        payload = json.dumps({
            "source_wallet_id": source_wallet_id,
            "destination_product_code": destination_product_code,
            "amount": {
                "currency": currency_code,
                "value": amount
            }
        })
        return self.get_essential_details(method, url, payload)
