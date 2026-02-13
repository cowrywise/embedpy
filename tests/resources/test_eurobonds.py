import json
from embed.resources.eurobonds import Eurobond
from unittest.mock import MagicMock, patch

@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_eurobonds(mock_get_essential_details, api_session):
    eb = Eurobond(api_session)
    mock_get_essential_details.return_value = MagicMock()
    eb.list_eurobonds(account_id="fake-acc")
    eb.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/eurobonds?account_id=fake-acc",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_eurobond_preview(mock_get_essential_details, api_session):
    eb = Eurobond(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"asset_code": "EB-1", "amount": 1000}
    eb.create_preview(**test_data)
    eb.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/eurobonds/preview",
        json.dumps(test_data),
    )
