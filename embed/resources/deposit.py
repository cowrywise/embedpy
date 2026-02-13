import json

from embed.common import APIResponse


class Deposit(APIResponse):
    """
    Handles all queries for Deposits including listing and retrieving.
    """

    def __init__(self, api_session):
        super(Deposit, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_deposits(self, **kwargs):
        """
        Retrieve a list of all deposits.

        Args:
            **kwargs: Arbitrary keyword arguments for filtering and pagination.
            page_size (int): Optional.
            page (int): Optional.
            all (bool): Optional. If True, return all without pagination.

        Returns:
            dict: The API response containing a list of deposits.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "deposits"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_deposit(self, deposit_id):
        """
        Retrieve details of a specific deposit.

        Args:
            deposit_id (str): The unique identifier for the deposit.

        Returns:
            dict: The API response containing deposit details.
        """
        method = "GET"
        url = self.base_url + f"deposits/{deposit_id}"
        return self.get_essential_details(method, url)
