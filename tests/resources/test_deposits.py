from embed.resources.deposit import Deposit
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_deposits(mock_get_essential_details, api_session):
    d = Deposit(api_session)
    mock_get_essential_details.return_value = MagicMock()
    d.list_deposits(all=True)
    d.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/deposits?all=True",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_deposit(mock_get_essential_details, api_session):
    d = Deposit(api_session)
    mock_get_essential_details.return_value = MagicMock()
    d.get_deposit("fake-d-id")
    d.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/deposits/fake-d-id",
    )
