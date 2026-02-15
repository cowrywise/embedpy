import json
from embed.common import APIResponse


class WithdrawalIntent(APIResponse):
    """
    Handles withdrawal intents.
    """

    def __init__(self, api_session):
        super(WithdrawalIntent, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def create_withdrawal_intent(self, **kwargs):
        """
        Initiate a withdrawal intent.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The account ID.
            bank_id (str): Required. The bank ID.
            amount (float): Required. The amount to withdraw.
            currency (str): Required. The currency code.

        Returns:
            dict: The API response.
        """
        required = ["account_id", "bank_id", "amount", "currency"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "withdrawal-intents"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def list_withdrawal_intents(self, **kwargs):
        """
        Retrieve a list of withdrawal intents.

        Args:
            **kwargs: Arbitrary keyword arguments for filtering.
            account_id (str): Optional.
            currency (str): Optional.

        Returns:
            dict: The API response.
        """
        query_path = "&".join(f"{k}={v}" for k, v in kwargs.items())
        method = "GET"
        url = self.base_url + "withdrawal-intents"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def retry_withdrawal_intent(self, **kwargs):
        """
        Retry a failed withdrawal intent.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required.
            reference (str): Required.
            currency (str): Required.

        Returns:
            dict: The API response.
        """
        required = ["account_id", "reference", "currency"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "withdrawal-intents/retry"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def cancel_withdrawal_intent(self, **kwargs):
        """
        Cancel a pending withdrawal intent.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required.
            reference (str): Required.
            currency (str): Required.

        Returns:
            dict: The API response.
        """
        required = ["account_id", "reference", "currency"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        url = self.base_url + "withdrawal-intents/cancel"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
