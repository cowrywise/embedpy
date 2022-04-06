from embed.resources.transaction import Transaction
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_transfers(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.list_transfers(page_size=20)
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_deposits(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.list_deposits(page_size=20)
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/deposits?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_withdrawals(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.list_withdrawals(page_size=20)
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawals?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_transfer(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_transfer("fake-id")
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transfers/fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_deposit(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_deposit("fake-id")
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/deposits/fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_withdrawal(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_withdrawal("fake-id")
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawals/fake-id",
    )
