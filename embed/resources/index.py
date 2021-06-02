import json
from embed.common import APIResponse


class Index(APIResponse):
    """
    Handles all queries for Indices
    """

    def __init__(self, api_host, token, version):
        super(Index, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_indexes(self):
        method = "GET"
        url = self.api_host + "indexes"
        return self.get_essential_details(method, url)

    def get_index(self, index_id):
        method = "GET"
        url = self.api_host + f"indexes/{index_id}"
        return self.get_essential_details(method, url)

    def get_index_assets(self, asset_id):
        method = "GET"
        url = self.api_host + f"indexes/{asset_id}/assets"
        return self.get_essential_details(method, url)

    def create_custom_index(self, account_id, name, description, allocations):
        method = "POST"
        url = self.api_host + "indexes"
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
        url = self.api_host + f"indexes/{asset_id}"

        payload = json.dumps(
            {"allocations": json.loads(allocations), "account_id": account_id}
        )
        return self.get_essential_details(method, url, payload)
