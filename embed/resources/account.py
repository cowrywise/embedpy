import json
from embed.common import APIResponse
from embed.errors import ValidationError


class Account(APIResponse):
    """
    Handles all queries for Account
    """

    def __init__(self, api_session):
        super(Account, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def create_account(self, **kwargs):
        required = ["first_name", "last_name", "email"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")
        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )
        method = "POST"
        url = self.base_url + "accounts"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_accounts(self):
        method = "GET"
        url = self.base_url + "accounts"
        return self.get_essential_details(method, url)

    def get_account(self, account_id):
        method = "GET"
        url = self.base_url + f"accounts/{account_id}"
        return self.get_essential_details(method, url)

    def get_portfolio(self, account_id):
        """
        Get the portfolio that belongs to an account.
        The asset_id comes from calling get_all_assets() of Asset
        """
        method = "GET"
        url = self.base_url + f"accounts/{account_id}/portfolio"
        return self.get_essential_details(method, url)

    def update_address(self, **kwargs):
        """
        Update the address of an account
        country options: NG, GH, etc
        """
        required = [
            "account_id",
            "street",
            "lga",
            "area_code",
            "city",
            "state",
            "country",
        ]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/address"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def update_next_of_kin(self, **kwargs):
        """
        Update the next of kin details.
        gender options: M or F
        """
        required = [
            "account_id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "relationship",
            "gender",
        ]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/nok"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def update_profile(self, **kwargs):
        """
        Update a profile.
        Gender options: M or F
        """
        required = ["account_id"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/profile"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def update_identity(self, **kwargs):

        required = ["account_id", "identity_type", "identity_value"]
        for key in required:
            if key not in kwargs.keys():
                raise ValidationError(f"{key} is required.")

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/identity"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)
