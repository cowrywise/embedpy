import json
from embed.common import APIResponse


class Asset(APIResponse):
    """
    Handles all queries for Asset
    """

    def __init__(self, api_host, token, version):
        super(Asset, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def get_assets(self):
        """
        Get all the known assets
        """
        method = "GET"
        url = self.api_host + "assets"
        return self.get_essential_details(method, url)

    def get_filtered_assets(self, asset_type):
        """
        Filter assets by type:  tbills, mutual-fund, index
        """
        method = "GET"
        url = self.api_host + f"assets?asset_type={asset_type}"
        return self.get_essential_details(method, url)

    def get_asset(self, asset_id):
        """
        Get a single asset by id
        """
        method = "GET"
        url = self.api_host + f"assets/{asset_id}"
        return self.get_essential_details(method, url)