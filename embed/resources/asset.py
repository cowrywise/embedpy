"""TODO: fix this; get data"""
from embed.common import APIResponse


class Asset(APIResponse):
    """
    Handles all queries for Asset discovery.
    """

    def __init__(self, api_session):
        super(Asset, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_assets(self, **kwargs):
        """
        Retrieve a list of all available investment assets.

        Args:
            **kwargs: Arbitrary keyword arguments.
            country (str): Optional. ISO 2-letter country code (e.g., 'NG', 'GH').
            asset_type (str): Optional. Filter by asset type (e.g., 'tbills', 'mutual_funds').

        Returns:
            dict: The API response containing a list of assets.
        """
        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "assets"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_asset(self, asset_id):
        """
        Retrieve details of a single asset by its ID.

        Args:
            asset_id (str): The unique identifier for the asset.

        Returns:
            dict: The API response containing asset details.
        """
        method = "GET"
        url = self.base_url + f"assets/{asset_id}"
        return self.get_essential_details(method, url)
