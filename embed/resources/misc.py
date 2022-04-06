import json

from embed.common import APIResponse


class Misc(APIResponse):
    """
    Handles queries to /misc
    """

    def __init__(self, api_session):
        super(Misc, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def get_banks(self, **kwargs):
        """
        Optional pagination params:
          - page: int
          - page_size: int
        """

        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "misc/banks"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def process_purchase(self, reference: str):
        method = "POST"
        url = self.base_url + "misc/process-investment"
        payload = json.dumps({"reference": reference})
        return self.get_essential_details(method, url, payload)

    def process_sale(self, reference: str):
        method = "POST"
        url = self.base_url + "misc/process-liquidation"
        payload = json.dumps({"reference": reference})
        return self.get_essential_details(method, url, payload)

    def bank_transfer(self, **kwargs):
        required = ["amount", "bank_account_number"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "misc/bank-transfer"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def external_investment_funding(self, **kwargs):
        required = [
            "account_id",
            "account_email",
            "amount",
            "confirmed_amount",
            # "product_code",
            # "transaction_time",
            "transaction_reference",
        ]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "misc/investment/external-funding"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def transfer_processing_fee(self, **kwargs):
        required = ["amount", "source_product_code", "destination_asset_code"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "misc/transfer/processing-fees"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def withdrawal_processing_fee(self, **kwargs):
        required = ["amount", "wallet_id"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "misc/withdrawal/processing-fees"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
