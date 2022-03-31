import json
import typing as t

from embed.common import APIResponse
from embed.errors import ValidationError


class StockPortfolio(APIResponse):
    """
    Handles all queries for Stock Portfolios
    """

    def __init__(self, api_session):
        super(StockPortfolio, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_stock_portfolio(self, **kwargs):
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "stocks-portfolio"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_stock_portfolio(self, portfolio_id):
        method = "GET"
        url = self.base_url + f"stocks-portfolio/{portfolio_id}"
        return self.get_essential_details(method, url)

    def create_stock_portfolio(self, **kwargs):
        """
        `risk_class` can be any of: PRESERVE | BALANCED | GROW
        `investment_preference`: MINIMIZE_LOSSES | NEUTRAL
        """
        required = ["account_id", "risk_class", "investment_preference"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "stocks-portfolio"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    @staticmethod
    def _validate_kwargs(required, kwargs):
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")
