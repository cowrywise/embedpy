import json
import uuid
from embed.common import APIResponse


class Account(APIResponse):
    """
    Handles all queries for Account
    """

    def __init__(self, api_session):
        super(Account, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({
            "Authorization": f"Bearer {self.token}"
        })

    def create_account(self, first_name, last_name, email, idempotency_key=None):
        if idempotency_key:
            self._headers.update({"embed_idempotency_key": str(idempotency_key)})
        method = "POST"
        url = self.base_url + "accounts"

        payload = json.dumps(
            {"first_name": first_name, "last_name": last_name, "email": email}
        )
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

    def update_address(
        self, account_id, street, lga, area_code, city, state, country="NG"
    ):
        """
        Update the address of an account
        country options: NG, GH, etc
        """
        method = "POST"
        url = self.base_url + f"accounts/{account_id}/address"

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
        url = self.base_url + f"accounts/{account_id}/nok"

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
        url = self.base_url + f"accounts/{account_id}/profile"

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
        url = self.base_url + f"accounts/{account_id}/identity"

        payload = json.dumps(
            {"identity_type": identity_type, "identity_value": identity_value}
        )
        return self.get_essential_details(method, url, payload)
