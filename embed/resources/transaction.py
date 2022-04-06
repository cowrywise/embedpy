from embed.common import APIResponse


class Transaction(APIResponse):
    """
    Handles all queries for Wallet
    """

    def __init__(self, api_session):
        super(Transaction, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_transfers(self, **kwargs):
        """
        Can filter by
            - account_id ........... Investment account email
            - email ................ Investment account email
            - transfer_type ........ funding, liquidation, p2p, asset_payout
            - from_date ............ Date in ISO8601 format e.g YYYY-MM-DD
            - to_date .............. Date in ISO8601 format e.g YYYY-MM-DD
            - status ............... pending, successful, failed
            - asset_type ........... mutual-fund, crypto, tbills, wallet, savings, index
            - currency ............. Currency code in ISO-4217 format
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "transfers"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_transfer(self, transfer_id):
        method = "GET"
        url = self.base_url + f"transfers/{transfer_id}"
        return self.get_essential_details(method, url)

    def list_deposits(self, **kwargs):
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "deposits"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_deposit(self, deposit_id):
        method = "GET"
        url = self.base_url + f"deposits/{deposit_id}"
        return self.get_essential_details(method, url)

    def list_withdrawals(self, **kwargs):
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "withdrawals"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_withdrawal(self, withdrawal_id):
        method = "GET"
        url = self.base_url + f"withdrawals/{withdrawal_id}"
        return self.get_essential_details(method, url)
