from embed.resources.asset import Asset
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest
from tests.responses import json_responses



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_assets(mock_get_essential_details, api_session):
    asset = Asset(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_ASSETS_RESPONSE, status_code=200)
    test_data = {}
    response = asset.get_assets()
    assert response.data == json_responses.GET_ASSETS_RESPONSE and response.status_code == 200
    asset.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/assets",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_single_asset(mock_get_essential_details, api_session):
    asset = Asset(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses., status_code=200)
    test_data = {"asset_type": "mutual-fund"}
    response = asset.get_filtered_assets(
        asset_type=test_data.get("asset_type")
    )
    assert response.data == json_responses.MUTUAL_FUND_ASSET_RESPONSE and response.status_code == 200
    asset.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/assets?asset_type=mutual-fund",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_assets_by_filter(mock_get_essential_details, api_session):
    asset = Asset(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.MUTUAL_FUND_ASSET_RESPONSE, status_code=200)
    test_data = {"asset_type": "mutual-fund"}
    response = asset.get_filtered_assets(
        asset_type=test_data.get("asset_type")
    )
    assert response.data == json_responses.MUTUAL_FUND_ASSET_RESPONSE and response.status_code == 200
    asset.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/assets?asset_type=mutual-fund",
    )