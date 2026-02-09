import json
from embed.common import APIResponse


class Wallet(APIResponse):
    """
    Handles all queries for Wallet management and transfers.
    """

    def __init__(self, api_session):
        super(Wallet, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_wallets(self, **kwargs):
        """
        Retrieve a list of all wallets.

        Args:
            **kwargs: Arbitrary keyword arguments.
            page_size (int): Optional. Number of items per page.
            page (int): Optional. Current page number.

        Returns:
            dict: The API response containing a list of wallets.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "wallets"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_wallet(self, wallet_id):
        """
        Retrieve details of a specific wallet.

        Args:
            wallet_id (str): The unique identifier for the wallet.

        Returns:
            dict: The API response containing wallet details.
        """
        method = "GET"
        url = self.base_url + f"wallets/{wallet_id}"
        return self.get_essential_details(method, url)

    def create_wallet(self, **kwargs):
        """
        Create a new wallet for an account.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            currency_code (str): Required. Currency code (e.g., 'NGN', 'USD').
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing new wallet details.
        """

        required = ["account_id", "currency_code"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "wallets"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def transfer(self, **kwargs):
        """
        Transfer funds from a wallet to a product (e.g., investment).

        Args:
            **kwargs: Arbitrary keyword arguments.
            wallet_id (str): Required. The source wallet ID.
            product_code (str): Required. The destination product code.
            amount (float): Required. Amount to transfer.
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing transfer details.
        """
        required = ["wallet_id", "product_code", "amount"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        wallet_id = kwargs.pop("wallet_id")
        method = "POST"
        url = self.base_url + f"wallets/{wallet_id}/transfer"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

