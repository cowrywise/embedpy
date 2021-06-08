import json
import uuid
from embed.common import APIResponse


class Investment(APIResponse):
    """
    Handles all queries for Investment
    """

    def __init__(self, api_session):
        super(Investment, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_investments(self):
        method = "GET"
        url = self.base_url + "investments"
        return self.get_essential_details(method, url)

    def get_investment(self, investment_id):
        method = "GET"
        url = self.base_url + f"investments/{investment_id}"
        return self.get_essential_details(method, url)

    def get_filtered_investments(self, asset_type):
        method = "GET"
        url = self.base_url + f"investments?asset_type={asset_type}"
        return self.get_essential_details(method, url)

    def create_investment(self, account_id, asset_code, amount):
        method = "POST"
        self._headers.update({"embed_idempotency_key": str(uuid.uuid4())})
        url = self.base_url + "investments"

        payload = json.dumps(
            {"account_id": account_id, "asset_code": asset_code, "amount": amount}
        )
        return self.get_essential_details(method, url, payload)

    def liquidate_investment(self, investment_id, units):
        method = "POST"
        url = self.base_url + f"investments/{investment_id}/liquidate"

        payload = json.dumps({"units": units})
        return self.get_essential_details(method, url, payload)
