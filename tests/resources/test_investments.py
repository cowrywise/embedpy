from embed.resources.investment import Investment
from unittest.mock import MagicMock, patch
import json


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_investments(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.list_investments()
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
    investment.list_investments(asset_type="tbills")
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
        "idempotency_key": "test_idempotency_key",
    }
    investment.create_investment(**test_data)
    idp_key = investment._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
    investment.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/investments",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_liquidate_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "investment_id": "fake-investment-id",
        "units": "200",
        "idempotency_key": "test_idempotency_key",
    }
    investment.liquidate_investment(**test_data)
    idp_key = investment._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
    investment.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/"
        f"fake-investment-id/liquidate",
        json.dumps({"units": "200"}),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_investment_holdings(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.get_investment_holdings("fake-investment-id")
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/"
        f"fake-investment-id/holdings",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_investment_performance(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.get_investment_performance("fake-investment-id")
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/"
        f"fake-investment-id/performance",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_investment_returns(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock()
    investment.get_investment_returns("fake-investment-id")
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/"
        f"fake-investment-id/returns",
    )
