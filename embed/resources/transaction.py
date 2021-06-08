from embed.common import APIResponse


class Transaction(APIResponse):
    """
    Handles all queries for Transaction
    """

    def __init__(self, api_session):
        super(Transaction, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_transactions(self):
        method = "GET"
        url = self.base_url + f"transactions"
        return self.get_essential_details(method, url)