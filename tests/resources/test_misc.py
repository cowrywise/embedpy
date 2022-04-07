import json
from unittest.mock import patch, MagicMock

from embed.resources.misc import Misc


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_banks(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    misc.get_banks(page_size=20)
    misc.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/banks?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_process_purchase(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"reference": "test_reference"}
    misc.process_purchase(**test_data)
    misc.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/process-investment",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_process_sale(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"reference": "test_reference"}
    misc.process_sale(**test_data)
    misc.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/process-liquidation",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_do_bank_transfer(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"amount": 5000, "bank_account_number": 1234567890}
    misc.bank_transfer(**test_data)
    misc.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/bank-transfer",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_external_investment_funding(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "test_account_id",
        "account_email": "test_account_email",
        "amount": 5000,
        "confirmed_amount": 5000,
        "transaction_reference": "test_transaction_reference",
    }
    misc.external_investment_funding(**test_data)
    misc.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/investment/external-funding",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_transfer_processing_fee(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "amount": 5000,
        "source_product_code": "test_source_product_code",
        "destination_asset_code": "test_destination_asset_code",
    }
    misc.transfer_processing_fee(**test_data)
    misc.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/transfer/processing-fees",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_withdrawal_processing_fee(mock_get_essential_details, api_session):
    misc = Misc(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"amount": 5000, "wallet_id": "test_wallet_id"}
    misc.withdrawal_processing_fee(**test_data)
    misc.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/misc/withdrawal/processing-fees",
        json.dumps(test_data),
    )
