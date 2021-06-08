import json
from embed.common import APIResponse


class Trade(APIResponse):
    """
    Handles all queries for Trade
    """

    def __init__(self, api_session):
        super(Trade, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_stocks(self):
        method = "GET"
        url = self.base_url + "stocks/assets"
        return self.get_essential_details(method, url)

    def get_single_position(self, account_id, stock_symbol):
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

    def buy_stock(self, symbol, amount, side, the_type, time_in_force, account_id, idempotency_key=None):
        method = "POST"
        url = self.base_url + "stocks/buy"
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
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

    def sell_stock(self, symbol, amount, side, the_type, time_in_force, account_id, idempotency_key=None):
        method = "POST"
        url = self.base_url + "stocks/sell"
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
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
        url = self.base_url + f"stocks/positions?account_id={account_id}"
        return self.get_essential_details(method, url)
