from embed.resources.wallet import Wallet
from unittest.mock import MagicMock, patch
import json


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_wallets(mock_get_essential_details, api_session):
    wallet = Wallet(api_session)
    mock_get_essential_details.return_value = MagicMock()
    wallet.list_wallets(page_size=20)
    wallet.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets?page_size=20",
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
    test_data = {
        "account_id": "fake-id",
        "currency_code": "NGN",
        "idempotency_key": "test_idempotency_key",
    }
    wallet.create_wallet(**test_data)
    idp_key = wallet._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
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
        "idempotency_key": "test_idempotency_key",
    }
    wallet.transfer(**test_data)
    idp_key = wallet._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
    wallet.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/wallets/fake-id/transfer",
        json.dumps({"product_code": "PRCD", "amount": "100000"}),
    )
