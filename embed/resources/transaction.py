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

    def get_transfers(self, transfer_id=None, **kwargs):

        # check that a query param is not empty and join it to the string.
        query_path = "&".join("{}={}".format(key, value) for key, value in kwargs.items())
        method = "GET"
        if transfer_id:
            url = self.base_url + f"transfers/{transfer_id}"
        else:
            url = self.base_url + "transfers"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_deposits(self):
        method = "GET"
        url = self.base_url + "deposits"
        return self.get_essential_details(method, url)

    def get_withdrawals(self):
        method = "GET"
        url = self.base_url + "withdrawals"
        return self.get_essential_details(method, url)
