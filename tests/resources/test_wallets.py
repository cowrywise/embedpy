from embed.resources.wallet import Wallet
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest
from tests.responses import json_responses



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_wallets(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    wallet.get_wallets()
    wallet.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_single_wallet(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    wallet.get_wallet("fake-id")
    wallet.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets/fake-id",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_create_wallet(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"account_id":"fake-id", "currency_code":"NGN"}
    wallet.create_wallet(account_id=test_data.get("account_id"), currency_code=test_data.get("currency_code"))
    wallet.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets",
        json.dumps(test_data)
    )