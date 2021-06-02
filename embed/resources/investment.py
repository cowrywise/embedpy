import json
from embed.common import APIResponse


class Investment(APIResponse):
    """
    Handles all queries for Investment
    """

    def __init__(self, api_host, token, version):
        super(Investment, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_investments(self):
        method = "GET"
        url = self.api_host + "investments"
        return self.get_essential_details(method, url)

    def get_investment(self, investment_id):
        method = "GET"
        url = self.api_host + f"investments/{investment_id}"
        return self.get_essential_details(method, url)

    def get_filtered_investments(self, asset_type):
        method = "GET"
        url = self.api_host + f"investments?asset_type={asset_type}"
        return self.get_essential_details(method, url)

    def create_investment(self, account_id, asset_code, amount):
        method = "POST"
        url = self.api_host + "investments"

        payload = json.dumps(
            {"account_id": account_id, "asset_code": asset_code, "amount": amount}
        )
        return self.get_essential_details(method, url, payload)

    def liquidate_investment(self, investment_id, units):
        method = "POST"
        url = self.api_host + f"investments/{investment_id}/liquidate"

        payload = json.dumps({"units": units})
        return self.get_essential_details(method, url, payload)
