import json
from datetime import datetime

from embed.common import APIResponse
from embed.errors import ValidationError


class Saving(APIResponse):
    """
    Handles all queries for Saving
    """

    def __init__(self, api_session):
        super(Saving, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def create_savings(self, **kwargs):

        required = ["account_id", "days", "interest_enabled", "currency_code"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "savings"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def list_savings(self, **kwargs):
        query_path = "&".join(
            "{}={}".format(key, value) for key, value in kwargs.items()
        )
        method = "GET"
        url = self.base_url + "savings"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_savings(self, savings_id):
        method = "GET"
        url = self.base_url + f"savings/{savings_id}"
        return self.get_essential_details(method, url)

    def get_savings_rates(self, days):
        method = "POST"
        url = self.base_url + f"savings/rates"
        payload = json.dumps({"days": days})
        return self.get_essential_details(method, url, payload)

    def get_savings_returns(
        self,
        savings_id,
        start_date: str = None,
        end_date: str = None
    ):
        params = {}
        try:
            if start_date:
                datetime.strptime(start_date, "%Y-%m-%d")
                params["start_date"] = start_date
            if end_date:
                datetime.strptime(end_date, "%Y-%m-%d")
                params["end_date"] = end_date
        except Exception:
            ValidationError(f"start_date and end_date should be in `YYYY-MM-DD` format.")

        method = "GET"
        url = self.base_url + f"savings/{savings_id}/returns"
        query_path = "&".join("{}={}".format(k, v) for k, v in params.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_savings_performance(
        self,
        savings_id,
        start_date: str = None,
        end_date: str = None
    ):
        params = {}
        try:
            if start_date:
                datetime.strptime(start_date, "%Y-%m-%d")
                params["start_date"] = start_date
            if end_date:
                datetime.strptime(end_date, "%Y-%m-%d")
                params["end_date"] = end_date
        except Exception:
            ValidationError(f"start_date and end_date should be in `YYYY-MM-DD` format.")

        method = "GET"
        url = self.base_url + f"savings/{savings_id}/performance"
        query_path = "&".join("{}={}".format(k, v) for k, v in params.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def withdraw(self, savings_id, amount):
        method = "POST"
        url = self.base_url + f"savings/{savings_id}/withdraw"
        payload = json.dumps({"amount": amount})
        return self.get_essential_details(method, url, payload)

    def rollover(self, savings_id, days):
        method = "POST"
        url = self.base_url + f"savings/{savings_id}/rollover"
        payload = json.dumps({"days": days})
        return self.get_essential_details(method, url, payload)
