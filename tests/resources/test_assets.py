from embed.resources.asset import Asset
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_assets(mock_get_essential_details, api_session):
    asset = Asset(api_session)
    mock_get_essential_details.return_value = MagicMock()
    asset.get_assets()
    asset.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/assets",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_assets_by_filter(mock_get_essential_details, api_session):
    asset = Asset(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"asset_type": "mutual-fund"}
    asset.get_assets(asset_type=test_data.get("asset_type"))
    asset.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/assets?asset_type=mutual-fund",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_asset(mock_get_essential_details, api_session):
    asset = Asset(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"asset_id": "fake-asset-id"}
    asset.get_asset(asset_id=test_data.get("asset_id"))
    asset.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/assets/fake-asset-id",
    )
