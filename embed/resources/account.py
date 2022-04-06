import json
from embed.common import APIResponse


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
        self._validate_kwargs(required, kwargs)
        if "idempotency_key" in kwargs.keys():
            self._headers.update(
                {"Embed-Idempotency-Key": str(kwargs.pop("idempotency_key"))}
            )
        method = "POST"
        url = self.base_url + "accounts"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def list_accounts(self, **kwargs):
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "accounts"
        if query_path:
            url = f"{url}?{query_path}"
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

    def get_portfolio_performance(self, **kwargs):
        """
        Get the performance of a portfolio
        """
        required = ["account_id", "currency"]
        # optional = ["start_date", "end_date"]

        self._validate_kwargs(required, kwargs)
        query_path = self._format_query(kwargs)
        method = "GET"
        url = (
            self.base_url + f"accounts/{kwargs.get('account_id')}/portfolio/performance"
        )
        if query_path:
            url = f"{url}?{query_path}"
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
        self._validate_kwargs(required, kwargs)

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
        self._validate_kwargs(required, kwargs)

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
        self._validate_kwargs(required, kwargs)

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/profile"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def update_identity(self, **kwargs):

        required = ["account_id", "identity_type", "identity_value"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/identity"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def add_bank_account(self, **kwargs):
        """
        Add a bank account to profile.
        The bank_code can be gotten from calling get_banks() of Misc
        """
        required = ["account_id", "bank_code", "account_number"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/bank"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_risk_profile_questions(self):
        """
        Get questions to used to determine risk profile of user
        """
        method = "GET"
        url = self.base_url + "accounts/risk-profile-questions"
        return self.get_essential_details(method, url)

    def update_risk_profile(self, **kwargs):
        """
        Post answers to risk profile questions and get risk score
        """
        required = ["account_id", "q1", "q2", "q3", "q4", "q5", "q6"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/risk-profile"

        kwargs = {int(k.replace("q", "")): kwargs.pop(k) for k in required[1:]}
        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def get_risk_profile(self, account_id):
        """
        Get a customer's risk profile
        """
        method = "GET"
        url = self.base_url + f"accounts/{account_id}/risk-profile"
        return self.get_essential_details(method, url)
