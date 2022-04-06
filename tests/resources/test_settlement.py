import json
from unittest.mock import patch, MagicMock

from embed.resources.settlement import Settlement


@patch("embed.common.APIResponse.get_essential_details")
def test_can_withdraw_to_bank(mock_get_essential_details, api_session):
    settlement = Settlement(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"account_id": "fake_id", "amount": 5000, "bank_id": "test_bank_id"}
    settlement.withdraw_to_bank(**test_data)
    settlement.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/settlements",
        json.dumps(test_data),
    )
