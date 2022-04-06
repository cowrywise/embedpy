import json

from embed.common import APIResponse


class Settlement(APIResponse):
    """
    Handles all queries for Settlements
    """

    def __init__(self, api_session):
        super(Settlement, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def withdraw_to_bank(self, **kwargs):
        required = ["account_id", "amount", "bank_id"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "settlements"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
