import json
from embed.common import APIResponse

class Eurobond(APIResponse):
    """
    Handles all queries for Eurobond investments.
    """

    def __init__(self, api_session):
        super(Eurobond, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_eurobonds(self, **kwargs):
        """
        Retrieve a list of all eurobond investments.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "eurobonds"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_eurobond(self, eurobond_id):
        """
        Retrieve details of a specific eurobond.
        """
        method = "GET"
        url = self.base_url + f"eurobonds/{eurobond_id}"
        return self.get_essential_details(method, url)

    def create_preview(self, **kwargs):
        """
        Get a preview of a eurobond investment.
        """
        method = "POST"
        url = self.base_url + "eurobonds/preview"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def create_eurobond(self, **kwargs):
        """
        Create a new eurobond investment.
        """
        required = ["account_id", "asset_code", "amount"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "eurobonds"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def withdraw_preview(self, eurobond_id, **kwargs):
        """
        Get a preview of a eurobond withdrawal.
        """
        method = "POST"
        url = self.base_url + f"eurobonds/{eurobond_id}/withdraw/preview"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def withdraw(self, eurobond_id, **kwargs):
        """
        Withdraw from a eurobond investment.
        """
        method = "POST"
        url = self.base_url + f"eurobonds/{eurobond_id}/withdraw"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
