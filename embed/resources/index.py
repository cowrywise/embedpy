import json
from embed.common import APIResponse


class Index(APIResponse):
    """
    Handles all queries for Indices management including custom index creation and modification.
    """

    def __init__(self, api_session):
        super(Index, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_indexes(self, **kwargs):
        """
        Retrieve a list of all available indices.

        Args:
            **kwargs: Arbitrary keyword arguments for pagination.
            page_size (int): Optional.
            page (int): Optional.

        Returns:
            dict: The API response containing a list of indices.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "indexes"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_index(self, index_id):
        """
        Retrieve details of a specific index.

        Args:
            index_id (str): The unique identifier for the index.

        Returns:
            dict: The API response containing index details.
        """
        method = "GET"
        url = self.base_url + f"indexes/{index_id}"
        return self.get_essential_details(method, url)

    def get_index_assets(self, asset_id):
        """
        Retrieve assets contained within a specific index.

        Args:
            asset_id (str): The unique identifier for the index (asset).

        Returns:
            dict: The API response containing a list of assets in the index.
        """
        method = "GET"
        url = self.base_url + f"indexes/{asset_id}/assets"
        return self.get_essential_details(method, url)

    def create_custom_index(self, **kwargs):
        """
        Create a custom index for a user.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            name (str): Required. Name of the custom index.
            description (str): Required. Description of the index.
            allocations (list): Required. List of asset codes and their weights.
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing new custom index details.
        """
        required = ["account_id", "name", "description", "allocations"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "indexes"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def modify_custom_index(self, **kwargs):
        """
        Modify an existing custom index.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            index_id (str): Required. The unique identifier for the index to modify.
            allocations (list): Optional. Updated list of asset codes and weights.

        Returns:
            dict: The API response containing updated index details.
        """
        required = ["account_id", "index_id"]
        self._validate_kwargs(required, kwargs)

        method = "PUT"
        index_id = kwargs.pop("index_id")
        url = self.base_url + f"indexes/{index_id}"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
