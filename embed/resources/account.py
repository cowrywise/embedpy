import json
from embed.common import APIResponse


class Account(APIResponse):
    """
    Handles all queries for Account
    """

    def __init__(self, api_host, token, version):
        super(Account, self).__init__()
        self.api_host = f"{api_host}/api/{version}/"
        self.token = token
        self._headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def create(self, first_name, last_name, email):
        method = "POST"
        url = self.api_host + "accounts"

        payload = json.dumps(
            {"first_name": first_name, "last_name": last_name, "email": email}
        )
        return self.get_essential_details(method, url, payload)

    def get_accounts(self):
        method = "GET"
        url = self.api_host + "accounts"
        return self.get_essential_details(method, url)

    def get_account(self, account_id):
        method = "GET"
        url = self.api_host + f"accounts/{account_id}"
        return self.get_essential_details(method, url)

    def get_portfolio(self, account_id, asset_id):
        """
        Get the portfolio that belongs to an account.
        The asset_id comes from calling get_all_assets() of Asset
        """
        method = "GET"
        url = self.api_host + f"accounts/{account_id}/portfolio"
        payload = json.dumps({"asset_id": asset_id})
        return self.get_essential_details(method, url, payload)

    def update_address(
        self, account_id, street, lga, area_code, city, state, country="NG"
    ):
        """
        Update the address of an account
        country options: NG, GH, etc
        """
        method = "POST"
        url = self.api_host + f"accounts/{account_id}/address"

        payload = json.dumps(
            {
                "street": street,
                "lga": lga,
                "area_code": area_code,
                "city": city,
                "state": state,
                "country": country,
            }
        )
        return self.get_essential_details(method, url, payload)

    def update_next_of_kin(
        self,
        account_id,
        email,
        first_name,
        last_name,
        phone_number,
        relationship,
        gender=None,
    ):
        """
        Update the next of kin details.
        gender options: M or F
        """
        method = "POST"
        url = self.api_host + f"accounts/{account_id}/nok"

        payload = json.dumps(
            {
                "email": email,
                "first_name": first_name,
                "gender": gender,
                "last_name": last_name,
                "phone_number": phone_number,
                "relationship": relationship,
            }
        )

        return self.get_essential_details(method, url, payload)

    def update_profile(
        self,
        account_id,
        email,
        first_name,
        last_name,
        phone_number,
        date_of_birth,
        gender=None,
    ):
        """
        Update a profile.
        Gender options: M or F
        """
        method = "POST"
        url = self.api_host + f"accounts/{account_id}/profile"

        payload = json.dumps(
            {
                "phone_number": phone_number,
                "date_of_birth": date_of_birth,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
            }
        )
        return self.get_essential_details(method, url, payload)

    def update_identity(self, account_id, identity_type, identity_value):
        method = "POST"
        url = self.api_host + f"accounts/{account_id}/identity"

        payload = json.dumps(
            {"identity_type": identity_type, "identity_value": identity_value}
        )
        return self.get_essential_details(method, url, payload)
