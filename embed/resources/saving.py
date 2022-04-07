import json

from embed.common import APIResponse


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
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "savings"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def list_savings(self, **kwargs):
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "savings"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_savings(self, savings_id):
        method = "GET"
        url = self.base_url + f"savings/{savings_id}"
        return self.get_essential_details(method, url)

    def get_savings_rates(self, days: int):
        method = "POST"
        url = self.base_url + "savings/rates"
        payload = json.dumps({"days": days})
        return self.get_essential_details(method, url, payload)

    def get_savings_returns(
        self, savings_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        if start_date:
            kwargs["start_date"] = self._validate_date_string(start_date)
        if end_date:
            kwargs["end_date"] = self._validate_date_string(end_date)

        method = "GET"
        url = self.base_url + f"savings/{savings_id}/returns"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_savings_performance(
        self, savings_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        if start_date:
            kwargs["start_date"] = self._validate_date_string(start_date)
        if end_date:
            kwargs["end_date"] = self._validate_date_string(end_date)

        method = "GET"
        url = self.base_url + f"savings/{savings_id}/performance"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
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
