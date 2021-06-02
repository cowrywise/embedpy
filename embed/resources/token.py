from embed.common import APIResponse


class Token(APIResponse):
    """
    Class to generate token using client credentials
    """

    def __init__(self, client_id, client_secret, base_url):
        super(Token, self).__init__()

        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.token_url = f"{self.base_url}/o/token/"

        self.grant_type = "client_credentials"
        self._headers.update({"Content-Type": "application/x-www-form-urlencoded"})

    def get_access_token(self):
        payload = f"grant_type={self.grant_type}&client_id={self.client_id}&client_secret={self.client_secret}"
        response, status = self.request("POST", self.token_url, self._headers, post_data=payload)
        return response.get("access_token"), status
