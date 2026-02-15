from embed.resources.withdrawal import Withdrawal
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_withdrawals(mock_get_essential_details, api_session):
    w = Withdrawal(api_session)
    mock_get_essential_details.return_value = MagicMock()
    w.list_withdrawals(page=1)
    w.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawals?page=1",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_withdrawal(mock_get_essential_details, api_session):
    w = Withdrawal(api_session)
    mock_get_essential_details.return_value = MagicMock()
    w.get_withdrawal("fake-w-id")
    w.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawals/fake-w-id",
    )



