from embed.resources.account import Account
from unittest.mock import MagicMock
import json


def test_can_create_account(api_session):
    account = Account(api_session)
    account.get_essential_details = MagicMock()
    test_data = {"first_name": "test", "last_name": "tester", "email": "tester@abc.com"}
    account.create_account(
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        email=test_data.get("email"),
    )
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts",
        json.dumps(test_data),
    )


def test_can_get_accounts(api_session):
    account = Account(api_session)
    account.get_essential_details = MagicMock()
    account.get_accounts()
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts",
    )


def test_can_get_single_account(api_session):
    account = Account(api_session)
    account.get_essential_details = MagicMock()
    account.get_account("id")
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/id",
    )


def test_can_get_portfolio(api_session):
    account = Account(api_session)
    account.get_essential_details = MagicMock()
    account.get_portfolio("fake_id")
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/portfolio",
    )
