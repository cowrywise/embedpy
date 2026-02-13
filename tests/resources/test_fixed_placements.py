import json
from embed.resources.fixed_placements import FixedPlacement
from unittest.mock import MagicMock, patch

@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_fixed_placements(mock_get_essential_details, api_session):
    fp = FixedPlacement(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fp.list_fixed_placements(account_id="fake-acc")
    fp.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-placements?account_id=fake-acc",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_fixed_placement_preview(mock_get_essential_details, api_session):
    fp = FixedPlacement(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"asset_code": "FP-1", "amount": 5000}
    fp.create_preview(**test_data)
    fp.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-placements/preview",
        json.dumps(test_data),
    )
