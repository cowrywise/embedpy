import json
from embed.common import APIResponse


class Account(APIResponse):
    """
    Handles all queries for Account management including creation, profile updates,
    identity verification, and risk profiling.
    """

    def __init__(self, api_session):
        super(Account, self).__init__()
        self.base_url = f"{api_session.base_url}/api/{api_session.api_version}/"
        self.token = api_session.token
        self._headers.update({"Authorization": f"Bearer {self.token}"})

    def create_account(self, **kwargs):
        """
        Create a new investment account.

        Args:
            **kwargs: Arbitrary keyword arguments.
            first_name (str): Required. Customer's first name.
            last_name (str): Required. Customer's last name.
            email (str): Required. Customer's email address.
            phone_number (str): Optional. Customer's phone number.
            terms_of_use_accepted (bool): Optional. Defaults to False. If True, accepts T&C.
            idempotency_key (str): Optional. Unique key to prevent duplicate requests.

        Returns:
            dict: The API response containing account details.
        """
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
        """
        List all accounts with optional filtering.

        Args:
            **kwargs: Arbitrary keyword arguments for pagination and filtering.
            page_size (int): Optional. Number of items per page.
            page (int): Optional. Current page number.

        Returns:
            dict: The API response containing a list of accounts.
        """
        query_path = self._format_query(kwargs)
        method = "GET"
        url = self.base_url + "accounts"
        if query_path:
            url = f"{url}?{query_path}"
        return self.get_essential_details(method, url)

    def get_account(self, account_id):
        """
        Retrieve a single account by its ID.

        Args:
            account_id (str): The unique identifier for the account.

        Returns:
            dict: The API response containing account details.
        """
        method = "GET"
        url = self.base_url + f"accounts/{account_id}"
        return self.get_essential_details(method, url)

    def get_portfolio(self, account_id):
        """
        Get the investment portfolio belonging to an account.

        Args:
            account_id (str): The unique identifier for the account.

        Returns:
            dict: The API response containing portfolio details.
        """
        method = "GET"
        url = self.base_url + f"accounts/{account_id}/portfolio"
        return self.get_essential_details(method, url)

    def get_portfolio_performance(self, **kwargs):
        """
        Get the performance history of a portfolio.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            currency (str): Required. Currency code (e.g., 'NGN', 'USD').
            start_date (str): Optional. Start date in YYYY-MM-DD format.
            end_date (str): Optional. End date in YYYY-MM-DD format.

        Returns:
            dict: The API response containing performance metrics.
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
        Update the physical address of an account holder.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            street (str): Required. Street address.
            lga (str): Required. Local Government Area.
            area_code (str): Required. Postal or area code.
            city (str): Required. City name.
            state (str): Required. State name.
            country (str): Required. ISO country code (e.g., 'NG', 'GH').

        Returns:
            dict: The API response containing updated account details.
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
        Update next of kin details for an account.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            email (str): Required. Email of the next of kin.
            first_name (str): Required. First name of the next of kin.
            last_name (str): Required. Last name of the next of kin.
            phone_number (str): Required. Phone number of the next of kin.
            relationship (str): Required. Relationship to the account holder.
            gender (str): Required. Gender ('M' or 'F').

        Returns:
            dict: The API response containing updated account details.
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
        Update the profile information of an account holder.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            first_name (str): Optional.
            last_name (str): Optional.
            phone_number (str): Optional.
            gender (str): Optional. 'M' or 'F'.
            date_of_birth (str): Optional. YYYY-MM-DD.

        Returns:
            dict: The API response containing updated profile details.
        """
        required = ["account_id"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/profile"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def update_identity(self, **kwargs):
        """
        Verify the identity of an account holder.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            identity_type (str): Required. Type of ID (e.g., 'bvn', 'nin').
            identity_value (str): Required. ID number.

        Returns:
            dict: The API response containing verification status.
        """

        required = ["account_id", "identity_type", "identity_value"]
        self._validate_kwargs(required, kwargs)

        method = "POST"
        account_id = kwargs.get("account_id")
        url = self.base_url + f"accounts/{account_id}/identity"

        payload = json.dumps(kwargs)
        return self.get_essential_details(method, url, payload)

    def add_bank_account(self, **kwargs):
        """
        Link a bank account to the user's profile.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            bank_code (str): Required. Bank code from Misc.get_banks().
            account_number (str): Required. 10-digit NUBAN.

        Returns:
            dict: The API response containing linked bank details.
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
        Fetch questions used to determine a user's risk profile.

        Returns:
            dict: The API response containing risk profile questions.
        """
        method = "GET"
        url = self.base_url + "accounts/risk-profile-questions"
        return self.get_essential_details(method, url)

    def update_risk_profile(self, **kwargs):
        """
        Submit answers to risk profile questions and retrieve a risk score.

        Args:
            **kwargs: Arbitrary keyword arguments.
            account_id (str): Required. The unique identifier for the account.
            q1 (int): Required. Answer to question 1.
            q2 (int): Required. Answer to question 2.
            q3 (int): Required. Answer to question 3.
            q4 (int): Required. Answer to question 4.
            q5 (int): Required. Answer to question 5.
            q6 (int): Required. Answer to question 6.

        Returns:
            dict: The API response containing the risk profile score.
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
        Retrieve a customer's calculated risk profile.

        Args:
            account_id (str): The unique identifier for the account.

        Returns:
            dict: The API response containing risk profile details.
        """
        method = "GET"
        url = self.base_url + f"accounts/{account_id}/risk-profile"
        return self.get_essential_details(method, url)

