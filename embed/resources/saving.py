import json
from embed.common import APIResponse


class Saving(APIResponse):
    """
    Handles all queries for Saving
    """

    def __init__(self, api_host, token, version):
        super(Saving, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def create_savings(self, account_id, days, interest_enabled, currency_code="NGN"):
        method = "POST"
        url = self.api_host + "savings"

        payload = json.dumps(
            {
                "account_id": account_id,
                "currency_code": currency_code,
                "days": days,
                "interest_enabled": interest_enabled,
            }
        )
        return self.get_essential_details(method, url, payload)

    def get_savings(self):
        method = "GET"
        url = self.api_host + "savings"
        return self.get_essential_details(method, url)

    def get_individual_savings(self, savings_id):
        method = "GET"
        url = self.api_host + f"savings/{savings_id}"
        return self.get_essential_details(method, url)
