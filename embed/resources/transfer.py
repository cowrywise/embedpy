import json
import uuid
from embed.common import APIResponse
from embed.errors import ValidationError


class Transfer(APIResponse):
    """
    Handles all queries for Wallet
    """

    def __init__(self, api_session):
        super(Transfer, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def get_transfers(self):
        method = "GET"
        url = self.base_url + "transfers"
        return self.get_essential_details(method, url)

    def get_deposits(self):
        method = "GET"
        url = self.base_url + "deposits"
        return self.get_essential_details(method, url)

    def get_withdrawals(self):
        method = "GET"
        url = self.base_url + "withdrawals"
        return self.get_essential_details(method, url)

    def get_transfer(self, transfer_id):
        method = "GET"
        url = self.base_url + f"transfers/{transfer_id}"
        return self.get_essential_details(method, url)

    def initiate_transfer(self, **kwargs):

        required = [
            "source_wallet_id",
            "destination_product_code",
            "amount",
            "currency_code",
        ]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        currency_code = kwargs.pop("currency_code")
        amount = kwargs.pop("amount")

        kwargs.update({"amount": {"currency": currency_code, "value": amount}})

        method = "POST"
        url = self.base_url + "transfers"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
