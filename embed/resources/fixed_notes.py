import json

from embed.common import APIResponse


class FixedNote(APIResponse):
    """
    Handles all queries for Fixed Notes management including creation, withdrawal, rollover, and performance tracking.
    """

    def __init__(self, api_session):
        super(FixedNote, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_fixed_notes(self, **kwargs):
        """
        Retrieve a list of all fixed notes.

        Args:
            **kwargs: Arbitrary keyword arguments for pagination.
            page_size (int): Optional.
            page (int): Optional.

        Returns:
            dict: The API response containing a list of fixed notes.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "fixed-notes"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_fixed_note(self, fixed_note_id):
        """
        Retrieve details of a specific fixed note.

        Args:
            fixed_note_id (str): The unique identifier for the fixed note.

        Returns:
            dict: The API response containing fixed note details.
        """
        method = "GET"
        url = self.base_url + f"fixed-notes/{fixed_note_id}"
        return self.get_essential_details(method, url)

    def create_fixed_note(self, **kwargs):
        """
        Create a new fixed note investment.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            asset_code (str): Required. The asset code for the fixed note.
            tenor_in_months (int): Required. Duration in months.
            amount_range (str): Required. Amount range (e.g., '10M-100M').
            auto_reinvest (bool): Optional. Whether to automatically reinvest.
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing new fixed note details.
        """
        required = ["account_id", "asset_code", "tenor_in_months", "amount_range"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "fixed-notes"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_fixed_note_rates(self, **kwargs):
        """
        Retrieve fixed note rates.

        Args:
            **kwargs: Arbitrary keyword arguments.
            tenor_in_months (int): Required. Duration in months.
            amount_range (str): Required. Amount range (e.g., '10M-100M').
            currency (str): Required. Currency code (e.g., 'NGN', 'USD').

        Returns:
            dict: The API response containing rate information.
        """
        required = ["tenor_in_months", "amount_range", "currency"]
        self._validate_kwargs(required, kwargs)

        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + f"fixed-notes/rates?{query_path}"
        return self.get_essential_details(method, url)

    def get_fixed_note_performance(
        self, fixed_note_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        """
        Retrieve performance timeseries for a fixed note.

        Args:
            fixed_note_id (str): The unique identifier for the fixed note.
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
        url = self.base_url + f"fixed-notes/{fixed_note_id}/performance"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_fixed_note_returns(
        self, fixed_note_id: str, start_date: str = None, end_date: str = None, **kwargs
    ):
        """
        Retrieve returns history for a fixed note.

        Args:
            fixed_note_id (str): The unique identifier for the fixed note.
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
        url = self.base_url + f"fixed-notes/{fixed_note_id}/returns"
        query_path = "&".join("{}={}".format(k, v) for k, v in kwargs.items())
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def withdraw(self, fixed_note_id, **kwargs):
        """
        Withdraw from a fixed note.

        Args:
            fixed_note_id (str): The unique identifier for the fixed note.
            amount (float): Optional. Specific amount to withdraw.
            liquidate_all (bool): Optional. Whether to liquidate all units.
            same_day_if_mature (bool): Optional. Whether to process same day if mature.

        Returns:
            dict: The API response containing withdrawal details.
        """
        method = "POST"
        url = self.base_url + f"fixed-notes/{fixed_note_id}/withdraw"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def rollover(self, fixed_note_id, tenor_in_months):
        """
        Rollover a fixed note for an additional period.

        Args:
            fixed_note_id (str): The unique identifier for the fixed note.
            tenor_in_months (int): Additional duration in months.

        Returns:
            dict: The API response containing rollover details.
        """
        method = "POST"
        url = self.base_url + f"fixed-notes/{fixed_note_id}/rollover"
        payload = json.dumps({"tenor_in_months": tenor_in_months})
        return self.get_essential_details(method, url, payload)

    def partial_update(self, fixed_note_id, **kwargs):
        """
        Partially update a fixed note.

        Args:
            fixed_note_id (str): The unique identifier for the fixed note.
            **kwargs: Fields to update (e.g., auto_reinvest).

        Returns:
            dict: The API response.
        """
        method = "PATCH"
        url = self.base_url + f"fixed-notes/{fixed_note_id}"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
