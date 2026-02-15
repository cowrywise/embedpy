import json
from embed.common import APIResponse


class Integration(APIResponse):
    """
    Handles external integrations like Atomic and CSCS.
    """

    def __init__(self, api_session):
        super(Integration, self).__init__()
        self.base_url = (
            f"{api_session.base_url}/api/{api_session.api_version}/integration/"
        )
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def cscs_onboarding(self, **kwargs):
        method = "POST"
        url = self.base_url + "cscs/onboarding"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_cscs_profile(self, account_id):
        method = "GET"
        url = self.base_url + f"cscs/onboarding?account_id={account_id}"
        return self.get_essential_details(method, url)
