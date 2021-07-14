from embed.common import APIResponse


class Price(APIResponse):
    """
    Handles all queries for Price
    """

    def __init__(self, api_session):
        super(Price, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def get_price_history(self, asset_id, from_date, to_date):
        """
        Get the price history of an asset
        The asset_id comes from calling get_all_assets() of Asset
        date-format: YYYY-MM-DD e.g. 2020-01-10
        """
        method = "GET"
        url = (
            self.base_url
            + f"prices?asset_id={asset_id}&from_date={from_date}&to_date={to_date}"
        )
        return self.get_essential_details(method, url)
