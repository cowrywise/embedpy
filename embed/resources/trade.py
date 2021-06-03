import json
from embed.common import APIResponse


class Trade(APIResponse):
    """
    Handles all queries for Trade
    """

    def __init__(self, api_host, token: str, version: str):
        super(Trade, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers = {
            "Authorization": f"Bearer {self.token}",
        }

    def get_stocks(self):
        method = "GET"
        url = self.api_host + "stocks/assets"
        return self.get_essential_details(method, url)

    def get_single_position(self, account_id, stock_symbol):
        method = "GET"
        url = self.api_host + f"stocks/{stock_symbol}/positions?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_orders(self, account_id):
        method = "GET"
        url = self.api_host + f"stocks/orders?account_id={account_id}&status=open"
        return self.get_essential_details(method, url)

    def get_profile(self, account_id):
        method = "GET"
        url = self.api_host + f"stocks/profile?account_id={account_id}"
        return self.get_essential_details(method, url)

    def get_position(self, account_id):
        method = "GET"
        url = self.api_host + f"stocks/positions?account_id={account_id}"
        return self.get_essential_details(method, url)

    def buy_stock(self, symbol, amount, side, the_type, time_in_force, account_id):
        method = "POST"
        url = self.api_host + "stocks/buy"

        payload = json.dumps(
            {
                "symbol": symbol,
                "amount": int(amount),
                "side": side,
                "type": the_type,
                "time_in_force": time_in_force,
                "account_id": account_id,
            }
        )
        return self.get_essential_details(method, url, payload)

    def sell_stock(self, symbol, amount, side, the_type, time_in_force, account_id):
        method = "POST"
        url = self.api_host + "stocks/sell"

        payload = json.dumps(
            {
                "symbol": symbol,
                "amount": int(amount),
                "side": side,
                "type": the_type,
                "time_in_force": time_in_force,
                "account_id": account_id,
            }
        )
        return self.get_essential_details(method, url, payload)

    def close_all_positions(self, account_id):
        method = "DELETE"
        url = self.api_host + f"stocks/positions?account_id={account_id}"
        return self.get_essential_details(method, url)
