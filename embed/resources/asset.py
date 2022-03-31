"""TODO: fix this; get data"""
from embed.common import APIResponse


class Asset(APIResponse):
    """
    Handles all queries for Asset
    """

    def __init__(self, api_session):
        super(Asset, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_assets(self, **kwargs):
        """
        Get all the known assets. Can also filter by country by supplying
        two-letter country code as "country" in kwarg
        """
        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "assets"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_asset(self, asset_id):
        """
        Get a single asset by id
        """
        method = "GET"
        url = self.base_url + f"assets/{asset_id}"
        return self.get_essential_details(method, url)
