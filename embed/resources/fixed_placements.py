import json
from embed.common import APIResponse


class FixedPlacement(APIResponse):
    """
    Handles all queries for Fixed Placement investments.
    """

    def __init__(self, api_session):
        super(FixedPlacement, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def list_fixed_placements(self, **kwargs):
        """
        Retrieve a list of all fixed placement investments.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "fixed-placements"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_fixed_placement(self, fixed_placement_id):
        """
        Retrieve details of a specific fixed placement.
        """
        method = "GET"
        url = self.base_url + f"fixed-placements/{fixed_placement_id}"
        return self.get_essential_details(method, url)

    def create_preview(self, **kwargs):
        """
        Get a preview of a fixed placement investment.
        """
        method = "POST"
        url = self.base_url + "fixed-placements/preview"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def create_fixed_placement(self, **kwargs):
        """
        Create a new fixed placement investment.
        """
        required = ["account_id", "asset_code", "amount"]
        self._validate_kwargs(required, kwargs)

        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )

        method = "POST"
        url = self.base_url + "fixed-placements"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def top_up_preview(self, fixed_placement_id, **kwargs):
        """
        Get a preview of a fixed placement top-up.
        """
        method = "POST"
        url = self.base_url + f"fixed-placements/{fixed_placement_id}/top-up/preview"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def withdraw_preview(self, fixed_placement_id, **kwargs):
        """
        Get a preview of a fixed placement withdrawal.
        """
        method = "POST"
        url = self.base_url + f"fixed-placements/{fixed_placement_id}/withdraw/preview"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def withdraw(self, fixed_placement_id, **kwargs):
        """
        Withdraw from a fixed placement investment.
        """
        method = "POST"
        url = self.base_url + f"fixed-placements/{fixed_placement_id}/withdraw"
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
