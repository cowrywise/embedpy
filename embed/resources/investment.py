import json
from embed.common import APIResponse
from embed.errors import ValidationError


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
        query_path = "&".join(
            "{}={}".format(key, value) for key, value in kwargs.items()
        )
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
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

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
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        investment_id = kwargs.pop("investment_id")
        url = self.base_url + f"investments/{investment_id}/liquidate"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
