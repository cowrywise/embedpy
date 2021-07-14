from embed.resources.transaction import Transaction
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_transfers(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_transfers()
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_deposits(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_deposits()
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/deposits",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_withdrawals(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_withdrawals()
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawals",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_transfer(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_transfers("fake-id")
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers/fake-id",
    )
