import json
from embed.common import APIResponse


class Investment(APIResponse):
    """
    Handles all queries for Investment including listing, creation, and liquidation.
    """

    def __init__(self, api_session):
        super(Investment, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_investments(self, **kwargs):
        """
        Retrieve a list of all investments.

        Args:
            **kwargs: Arbitrary keyword arguments.
            asset_type (str): Optional. Filter by asset type code (e.g., 'tbills', 'mutual_funds').
            page_size (int): Optional. Number of items per page.
            page (int): Optional. Current page number.

        Returns:
            dict: The API response containing a list of investments.
        """
        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "investments"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_investment(self, investment_id):
        """
        Retrieve details of a specific investment.

        Args:
            investment_id (str): The unique identifier for the investment.

        Returns:
            dict: The API response containing investment details.
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}"
        return self.get_essential_details(method, url)

    def create_investment(self, **kwargs):
        """
        Create a new investment.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            asset_code (str): Required. The code of the asset to invest in.
            amount (float): Optional. Amount to invest.
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing the new investment details.
        """
        required = ["account_id", "asset_code"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )
        method = "POST"
        url = self.base_url + "investments"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def liquidate_investment(self, **kwargs):
        """
        Liquidate an existing investment.

        Args:
            **kwargs: Arbitrary keyword arguments.
            investment_id (str): Required. The unique identifier for the investment.
            units (str): Required. Number of units to liquidate.
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing liquidation details.
        """
        required = ["investment_id", "units"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        investment_id = kwargs.pop("investment_id")
        url = self.base_url + f"investments/{investment_id}/liquidate"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_investment_holdings(self, investment_id):
        """
        Retrieve holdings details for an investment (specifically for Indexes).

        Args:
            investment_id (str): The unique identifier for the investment.

        Returns:
            dict: The API response containing holdings information.
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}/holdings"
        return self.get_essential_details(method, url)

    def get_investment_performance(self, investment_id):
        """
        Retrieve performance timeseries for an investment.

        Args:
            investment_id (str): The unique identifier for the investment.

        Returns:
            dict: The API response containing performance data.
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}/performance"
        return self.get_essential_details(method, url)

    def get_investment_returns(self, investment_id):
        """
        Retrieve returns history for an investment.

        Args:
            investment_id (str): The unique identifier for the investment.

        Returns:
            dict: The API response containing returns data.
        """
        method = "GET"
        url = self.base_url + f"investments/{investment_id}/returns"
        return self.get_essential_details(method, url)
