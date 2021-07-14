import json
from embed.common import APIResponse
from embed.errors import ValidationError


class Trade(APIResponse):
    """
    Handles all queries for Trade
    """

    def __init__(self, api_session):
        super(Trade, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def get_stocks(self):
        method = "GET"
        url = self.base_url + "stocks/assets"
        return self.get_essential_details(method, url)

    def get_single_position(self, **kwargs):
        required = ["account_id", "stock_symbol"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        account_id = kwargs.get("account_id")
        stock_symbol = kwargs.get("stock_symbol")

        method = "GET"
        url = self.base_url + f"stocks/{stock_symbol}/positions?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_orders(self, account_id):
        method = "GET"
        url = self.base_url + f"stocks/orders?account_id={account_id}&status=open"
        return self.get_essential_details(method, url)

    def get_profile(self, account_id):
        method = "GET"
        url = self.base_url + f"stocks/profile?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_position(self, account_id):
        method = "GET"
        url = self.base_url + f"stocks/positions?account_id={account_id}"
        return self.get_essential_details(method, url)

    def buy_stock(self, **kwargs):
        required = [
            "account_id",
            "symbol",
            "amount",
            "side",
            "the_type",
            "time_in_force",
        ]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        kwargs.update({"amount": int(kwargs.get("amount"))})
        method = "POST"
        url = self.base_url + "stocks/buy"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def sell_stock(self, **kwargs):
        required = [
            "account_id",
            "symbol",
            "amount",
            "side",
            "the_type",
            "time_in_force",
        ]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        kwargs.update({"amount": int(kwargs.get("amount"))})
        method = "POST"
        url = self.base_url + "stocks/sell"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def close_all_positions(self, account_id):
        method = "DELETE"
        url = self.base_url + f"stocks/positions?account_id={account_id}"
        return self.get_essential_details(method, url)
