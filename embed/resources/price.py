from embed.common import APIResponse


class Price(APIResponse):
    """
    Handles all queries for Price
    """

    def __init__(self, api_host, token, version):
        super(Price, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_price_history(self, asset_id, from_date, to_date):
        """
        Get the price history of an asset
        The asset_id comes from calling get_all_assets() of Asset
        date-format: YYYY-MM-DD e.g. 2020-01-10
        """
        method = "GET"
        url = (
            self.api_host
            + f"prices?asset_id={asset_id}&from_date={from_date}&to_date={to_date}"
        )
        return self.get_essential_details(method, url)
