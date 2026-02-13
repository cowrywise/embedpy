import json

from embed.common import APIResponse


class Withdrawal(APIResponse):
    """
    Handles all queries for Withdrawals including listing, retrieving, and managing withdrawal intents.
    """

    def __init__(self, api_session):
        super(Withdrawal, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_withdrawals(self, **kwargs):
        """
        Retrieve a list of all withdrawals.

        Args:
            **kwargs: Arbitrary keyword arguments for filtering and pagination.
            page_size (int): Optional.
            page (int): Optional.
            all (bool): Optional. If True, return all without pagination.

        Returns:
            dict: The API response containing a list of withdrawals.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "withdrawals"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_withdrawal(self, withdrawal_id):
        """
        Retrieve details of a specific withdrawal.

        Args:
            withdrawal_id (str): The unique identifier for the withdrawal.

        Returns:
            dict: The API response containing withdrawal details.
        """
        method = "GET"
        url = self.base_url + f"withdrawals/{withdrawal_id}"
        return self.get_essential_details(method, url)

    def list_withdrawal_intents(self, **kwargs):
        """
        Retrieve a list of all withdrawal intents.

        Args:
            **kwargs: Arbitrary keyword arguments for filtering.
            user_email (str): Optional. Filter by user email.
            currency (str): Optional. Filter by currency.

        Returns:
            dict: The API response containing a list of withdrawal intents.
        """
        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "withdrawals/intents"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def retry_withdrawal_intent(self, **kwargs):
        """
        Retry a failed withdrawal intent.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The account ID.
            withdrawal_intent_id (str): Required. The withdrawal intent ID.

        Returns:
            dict: The API response containing retry details.
        """
        required = ["account_id", "withdrawal_intent_id"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "withdrawals/intents/retry"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def cancel_withdrawal_intent(self, **kwargs):
        """
        Cancel a pending withdrawal intent.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The account ID.
            withdrawal_intent_id (str): Required. The withdrawal intent ID.

        Returns:
            dict: The API response containing cancellation details.
        """
        required = ["account_id", "withdrawal_intent_id"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "withdrawals/intents/cancel"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
