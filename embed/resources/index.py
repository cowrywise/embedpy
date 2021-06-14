import json
from embed.common import APIResponse
from embed.errors import ValidationError


class Index(APIResponse):
    """
    Handles all queries for Indices
    """

    def __init__(self, api_session):
        super(Index, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def get_indexes(self):
        method = "GET"
        url = self.base_url + "indexes"
        return self.get_essential_details(method, url)

    def get_index(self, index_id):
        method = "GET"
        url = self.base_url + f"indexes/{index_id}"
        return self.get_essential_details(method, url)

    def get_index_assets(self, asset_id):
        method = "GET"
        url = self.base_url + f"indexes/{asset_id}/assets"
        return self.get_essential_details(method, url)

    def create_custom_index(self, **kwargs):
        required = ["account_id", "name", "description", "allocations"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "indexes"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def modify_custom_index(self, **kwargs):
        required = ["account_id", "index_id"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        method = "PUT"
        index_id = kwargs.get("index_id")
        url = self.base_url + f"indexes/{index_id}"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
