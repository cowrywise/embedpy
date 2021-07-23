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
        query_path = "&".join("{}={}".format(key, value) for key, value in kwargs.items())
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
        query_path = "&".join("{}={}".format(key, value) for key, value in kwargs.items())
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
        query_path = "&".join("{}={}".format(key, value) for key, value in kwargs.items())
        method = "GET"
        url = self.base_url + "withdrawals"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_withdrawal(self, withdrawal_id):
        method = "GET"
        url = self.base_url + f"withdrawals/{withdrawal_id}"
        return self.get_essential_details(method, url)
