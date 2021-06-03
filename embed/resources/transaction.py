from embed.common import APIResponse


class Transaction(APIResponse):
    """
    Handles all queries for Transaction
    """

    def __init__(self, api_host, token, version):
        super(Transaction, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def get_transactions(self):
        method = "GET"
        url = self.api_host + f"transactions"
        return self.get_essential_details(method, url)