import json

from embed.common import APIResponse


class FlexibleSaving(APIResponse):
    """
    Handles all queries for Flexible Savings management including creation, withdrawal, and performance tracking.
    """

    def __init__(self, api_session):
        super(FlexibleSaving, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_flexible_savings(self, **kwargs):
        """
        Retrieve a list of all flexible savings plans.

        Args:
            **kwargs: Arbitrary keyword arguments for pagination.
            page_size (int): Optional.
            page (int): Optional.

        Returns:
            dict: The API response containing a list of flexible savings.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "flexible-savings"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_flexible_savings(self, flexible_savings_id):
        """
        Retrieve details of a specific flexible savings plan.

        Args:
            flexible_savings_id (str): The unique identifier for the flexible savings plan.

        Returns:
            dict: The API response containing flexible savings details.
        """
        method = "GET"
        url = self.base_url + f"flexible-savings/{flexible_savings_id}"
        return self.get_essential_details(method, url)

    def create_flexible_savings(self, **kwargs):
        """
        Create a new flexible savings plan.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            currency_code (str): Required. Currency code (e.g., 'NGN', 'USD').
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing new flexible savings details.
        """
        required = ["account_id", "currency_code"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "flexible-savings"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_flexible_savings_rates(self):
        """
        Retrieve the current flexible savings interest rate.

        Returns:
            dict: The API response containing rate information.
        """
        method = "GET"
        url = self.base_url + "flexible-savings/rates"
        return self.get_essential_details(method, url)

    def get_flexible_savings_performance(
        self, flexible_savings_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        """
        Retrieve performance timeseries for a flexible savings plan.

        Args:
            flexible_savings_id (str): The unique identifier for the flexible savings plan.
            start_date (str): Optional. YYYY-MM-DD.
            end_date (str): Optional. YYYY-MM-DD.
            **kwargs: Additional filtering parameters.

        Returns:
            dict: The API response containing performance data.
        """
        if start_date:
            kwargs["start_date"] = self._validate_date_string(start_date)
        if end_date:
            kwargs["end_date"] = self._validate_date_string(end_date)

        method = "GET"
        url = self.base_url + f"flexible-savings/{flexible_savings_id}/performance"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_flexible_savings_returns(
        self, flexible_savings_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        """
        Retrieve returns history for a flexible savings plan.

        Args:
            flexible_savings_id (str): The unique identifier for the flexible savings plan.
            start_date (str): Optional. YYYY-MM-DD.
            end_date (str): Optional. YYYY-MM-DD.
            **kwargs: Additional filtering parameters.

        Returns:
            dict: The API response containing returns data.
        """
        if start_date:
            kwargs["start_date"] = self._validate_date_string(start_date)
        if end_date:
            kwargs["end_date"] = self._validate_date_string(end_date)

        method = "GET"
        url = self.base_url + f"flexible-savings/{flexible_savings_id}/returns"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def withdraw(self, flexible_savings_id, amount):
        """
        Withdraw funds from a flexible savings plan.

        Args:
            flexible_savings_id (str): The unique identifier for the flexible savings plan.
            amount (float): The amount to withdraw.

        Returns:
            dict: The API response containing withdrawal details.
        """
        method = "POST"
        url = self.base_url + f"flexible-savings/{flexible_savings_id}/withdraw"
        payload = json.dumps({"amount": amount})
        return self.get_essential_details(method, url, payload)
