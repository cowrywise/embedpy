from embed.resources.account import Account
from unittest.mock import MagicMock
import json

from tests import responses
responses.crea







'''
const createAccountsResponse = require('../responses/create_account_200.json')
const getAccountsResponse = require('../responses/get_account_200.json')
const getSingleAccountsResponse = require('../responses/get_single_account_200.json')
const getPortfolioResponse = require('../responses/get_portfolio_200.json')
const updateAddressResponse = require('../responses/update_address_200.json')
const updateNokResponse = require('../responses/update_nok_200.json')
const updateProfileResponse = require('../responses/update_profile_200.json')
const updateIdentityResponse = require('../responses/update_identity_200.json')
const errorResponse = require('../responses/error_response_400_401.json')
'''

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
