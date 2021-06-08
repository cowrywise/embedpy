import json
from embed.common import APIResponse


class Asset(APIResponse):
    """
    Handles all queries for Asset
    """

    def __init__(self, api_session):
        super(Asset, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_assets(self):
        """
        Get all the known assets
        """
        method = "GET"
        url = self.base_url + "assets"
        return self.get_essential_details(method, url)

    def get_filtered_assets(self, asset_type):
        """
        Filter assets by type:  tbills, mutual-fund, index
        """
        method = "GET"
        url = self.base_url + f"assets?asset_type={asset_type}"
        return self.get_essential_details(method, url)

    def get_asset(self, asset_id):
        """
        Get a single asset by id
        """
        method = "GET"
        url = self.base_url + f"assets/{asset_id}"
        return self.get_essential_details(method, url)