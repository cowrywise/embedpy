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

    def get_transfers(
        self,
        transfer_id=None,
        account_id=None,
        transfer_type=None,
        from_date=None,
        to_date=None,
        status=None,
        asset_type=None,
        currency=None,
        email=None,
    ):
        query_list = [
            account_id,
            transfer_type,
            from_date,
            to_date,
            status,
            asset_type,
            currency,
            email,
        ]

        # check that a query param is not empty and join it to the string.
        query_path = "&".join(
            "{}={}".format(query_list[position], query)
            for position, query in enumerate(query_list)
            if query is not None
        )
        method = "GET"
        if transfer_id:
            url = self.base_url + f"transfers/{transfer_id}"
        else:
            url = self.base_url + "transfers"
        if query_path:
            url = f"{url}+?+{query_path}"
        return self.get_essential_details(method, url)

    def get_deposits(self):
        method = "GET"
        url = self.base_url + "deposits"
        return self.get_essential_details(method, url)

    def get_withdrawals(self):
        method = "GET"
        url = self.base_url + "withdrawals"
        return self.get_essential_details(method, url)
