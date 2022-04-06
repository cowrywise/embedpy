import json
from embed.common import APIResponse


class Investment(APIResponse):
    """
    Handles all queries for Investment
    """

    def __init__(self, api_session):
        super(Investment, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_investments(self, **kwargs):
        """
        Gets a list of investments. Filter result by asset-type by supplying
        the asset-type code as `asset_type` as kwarg
        """
        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "investments"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_investment(self, investment_id):
        method = "GET"
        url = self.base_url + f"investments/{investment_id}"
        return self.get_essential_details(method, url)

    def create_investment(self, **kwargs):
        required = ["account_id", "asset_code"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )
        method = "POST"
        url = self.base_url + "investments"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def liquidate_investment(self, **kwargs):
        required = ["investment_id", "units"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        investment_id = kwargs.pop("investment_id")
        url = self.base_url + f"investments/{investment_id}/liquidate"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_investment_holdings(self, investment_id):
        """
        For Indexes
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}/holdings"
        return self.get_essential_details(method, url)

    def get_investment_performance(self, investment_id):
        """
        Get investment performance timeseries
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}/performance"
        return self.get_essential_details(method, url)

    def get_investment_returns(self, investment_id):
        """
        Get investment performance timeseries
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}/returns"
        return self.get_essential_details(method, url)
