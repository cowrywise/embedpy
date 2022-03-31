from embed.common import APIResponse


class Misc(APIResponse):
    """
    Handles queries to /misc
    """

    def __init__(self, api_session):
        super(Misc, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def get_banks(self, page=None, page_size=None):
        query_params = {}
        if page:
            query_params["page"] = page
        if page_size:
            query_params["page_size"] = page_size

        query_path = "&".join(f"{k}={v}" for k, v in query_params.items())
        method = "GET"
        url = self.base_url + "misc/banks"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)
