import json

from embed.common import APIResponse


class Saving(APIResponse):
    """
    Handles all queries for Savings management including creation, withdrawal, and performance tracking.
    """

    def __init__(self, api_session):
        super(Saving, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def create_savings(self, **kwargs):
        """
        Create a new savings plan.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            days (int): Required. Duration of the savings plan in days.
            interest_enabled (bool): Required. Whether interest should be enabled.
            currency_code (str): Required. Currency code (e.g., 'NGN', 'USD').
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing new savings details.
        """

        required = ["account_id", "days", "interest_enabled", "currency_code"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "savings"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def list_savings(self, **kwargs):
        """
        Retrieve a list of all savings plans.

        Args:
            **kwargs: Arbitrary keyword arguments for pagination.
            page_size (int): Optional.
            page (int): Optional.

        Returns:
            dict: The API response containing a list of savings.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "savings"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_savings(self, savings_id):
        """
        Retrieve details of a specific savings plan.

        Args:
            savings_id (str): The unique identifier for the savings plan.

        Returns:
            dict: The API response containing savings details.
        """
        method = "GET"
        url = self.base_url + f"savings/{savings_id}"
        return self.get_essential_details(method, url)

    def get_savings_rates(self, days: int):
        """
        Retrieve savings rates for a specified duration.

        Args:
            days (int): The duration in days to check rates for.

        Returns:
            dict: The API response containing rate information.
        """
        method = "POST"
        url = self.base_url + "savings/rates"
        payload = json.dumps({"days": days})
        return self.get_essential_details(method, url, payload)

    def get_savings_returns(
        self, savings_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        """
        Retrieve returns history for a savings plan.

        Args:
            savings_id (str): The unique identifier for the savings plan.
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
        url = self.base_url + f"savings/{savings_id}/returns"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_savings_performance(
        self, savings_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        """
        Retrieve performance timeseries for a savings plan.

        Args:
            savings_id (str): The unique identifier for the savings plan.
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
        url = self.base_url + f"savings/{savings_id}/performance"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def withdraw(self, savings_id, amount):
        """
        Withdraw funds from a savings plan.

        Args:
            savings_id (str): The unique identifier for the savings plan.
            amount (float): The amount to withdraw.

        Returns:
            dict: The API response containing withdrawal details.
        """
        method = "POST"
        url = self.base_url + f"savings/{savings_id}/withdraw"
        payload = json.dumps({"amount": amount})
        return self.get_essential_details(method, url, payload)

    def rollover(self, savings_id, days):
        """
        Rollover a savings plan for an additional duration.

        Args:
            savings_id (str): The unique identifier for the savings plan.
            days (int): Additional duration in days.

        Returns:
            dict: The API response containing rollover details.
        """
        method = "POST"
        url = self.base_url + f"savings/{savings_id}/rollover"
        payload = json.dumps({"days": days})
        return self.get_essential_details(method, url, payload)
