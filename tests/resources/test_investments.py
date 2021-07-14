from embed.resources.investment import Investment
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_investments(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.get_investments()
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.get_investment("fake-investment-id")
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/fake-investment-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_filtered_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.get_investments(asset_type="tbills")
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments?asset_type=tbills",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "bbaaaaaabbb6477f866b20161e003ebb",
        "asset_code": "AST-TBILL-0001000000",
    }
    investment.create(
        account_id=test_data.get("account_id"), asset_code=test_data.get("asset_code")
    )
    investment.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/investments",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_liquidate_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"investment_id": "fake-investment-id", "units": "200"}
    investment.liquidate(
        investment_id=test_data.get("investment_id"), units=test_data.get("units")
    )
    investment.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/fake-investment-id/liquidate",
        json.dumps({"units": "200"}),
    )
