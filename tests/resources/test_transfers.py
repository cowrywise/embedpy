from embed.resources.transfer import Transfer
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_transfers(mock_get_essential_details, api_session):
    transfer = Transfer(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transfer.get_transfers()
    transfer.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_single_transfer(mock_get_essential_details, api_session):
    transfer = Transfer(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transfer.get_transfer("fake-id")
    transfer.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers/fake-id",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_initiate_transfer(mock_get_essential_details, api_session):
    transfer = Transfer(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "source_wallet_id": "fake-id",
        "destination_product_code": "PRCD",
        "amount": "100000",
        "currency_code": "NGN"
    }
    transfer.initiate_transfer(
        source_wallet_id=test_data.get("source_wallet_id"),
        destination_product_code=test_data.get("destination_product_code"),
        amount=test_data.get("amount"),
        currency_code=test_data.get("currency_code")
        )
    transfer.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers",
        json.dumps({
        "source_wallet_id": "fake-id",
        "destination_product_code": "PRCD",
        "amount": {"currency": "NGN", "value": "100000"}})
        )