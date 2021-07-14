from embed.resources.wallet import Wallet
from unittest.mock import MagicMock, patch
import json


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_wallets(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    wallet.get_wallets()
    wallet.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_wallet(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    wallet.get_wallet("fake-id")
    wallet.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets/fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_wallet(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"account_id": "fake-id", "currency_code": "NGN"}
    wallet.create_wallet(
        account_id=test_data.get("account_id"),
        currency_code=test_data.get("currency_code"),
    )
    wallet.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_transfer(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "wallet_id": "fake-id",
        "product_code": "PRCD",
        "amount": "100000",
    }
    wallet.transfer(
        wallet_id=test_data.get("wallet_id"),
        product_code=test_data.get("product_code"),
        amount=test_data.get("amount"),
    )
    wallet.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets/fake-id/transfer",
        json.dumps({"product_code": "PRCD", "amount": "100000"}),
    )
