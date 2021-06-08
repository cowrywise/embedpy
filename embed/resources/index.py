import json
import uuid
from embed.common import APIResponse


class Index(APIResponse):
    """
    Handles all queries for Indices
    """

    def __init__(self, api_session):
        super(Index, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

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

    def create_custom_index(self, account_id, name, description, allocations, idempotency_key=None):
        method = "POST"
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
        url = self.base_url + "indexes"
        payload = json.dumps(
            {
                "account_id": account_id,
                "name": name,
                "description": description,
                "allocations": json.loads(allocations),
            }
        )
        return self.get_essential_details(method, url, payload)

    def modify_custom_index(self, asset_id, account_id, allocations):
        method = "PUT"
        url = self.base_url + f"indexes/{asset_id}"

        payload = json.dumps(
            {"allocations": json.loads(allocations), "account_id": account_id}
        )
        return self.get_essential_details(method, url, payload)
