import json
import uuid
from embed.common import APIResponse


class Saving(APIResponse):
    """
    Handles all queries for Saving
    """

    def __init__(self, api_session):
        super(Saving, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def create_savings(self, account_id, days, interest_enabled, currency_code="NGN", idempotency_key=None):
        method = "POST"
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
        url = self.base_url + "savings"

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
        url = self.base_url + "savings"
        return self.get_essential_details(method, url)

    def get_individual_savings(self, savings_id):
        method = "GET"
        url = self.base_url + f"savings/{savings_id}"
        return self.get_essential_details(method, url)
