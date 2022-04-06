import json
import typing as t

from embed.common import APIResponse


class Stock(APIResponse):
    """
    Handles all queries for Stocks
    """

    def __init__(self, api_session):
        super(Stock, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_stocks(self, **kwargs):
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "stocks/assets"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_stocks(self, symbols: t.List[str], **kwargs):
        query_path = "&".join("symbol={}".format(s) for s in symbols)
        query_path += "&" + "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + f"stocks/assets?{query_path}"
        return self.get_essential_details(method, url)

    def buy_stocks(self, **kwargs):
        required = ["account_id", "symbol", "amount", "side", "type", "time_in_force"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "stocks/buy"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def sell_stocks(self, **kwargs):
        required = ["account_id", "symbol", "amount", "side", "type", "time_in_force"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "stocks/sell"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_profile(self, account_id: str):
        method = "GET"
        url = self.base_url + f"stocks/profile?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_positions(self, account_id: str):
        method = "GET"
        url = self.base_url + f"stocks/positions?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_position(self, account_id: str, symbol: str):
        method = "GET"
        url = self.base_url + f"stocks/positions/{symbol}?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_orders(self, account_id: str, status: str = "all"):
        """status can be `open`, `closed` or `all`"""
        method = "GET"
        url = self.base_url + f"stocks/orders?account_id={account_id}&status={status}"
        return self.get_essential_details(method, url)

    # def get_order(self, account_id: str):
    #     # TODO: get params from Rahman
    #     method = "GET"
    #     url = self.base_url + f"stocks/orders/?account_id={account_id}"
    #     return self.get_essential_details(method, url)
    #
    # def close_all_positions(self, account_id: str):
    #     # TODO: get params from Rahman
    #     method = "GET"
    #     url = self.base_url + f"stocks/positions?account_id={account_id}"
    #     return self.get_essential_details(method, url)
