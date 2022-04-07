import json

from embed.resources.saving import Saving
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_savings(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "days": "30",
        "interest_enabled": True,
        "currency_code": "NGN",
        "idempotency_key": "test_idempotency_key",
    }
    savings.create_savings(**test_data)
    idp_key = savings._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
    savings.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/savings",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_savings(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    savings.list_savings(page_size=20)
    savings.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/savings?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_savings(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    savings.get_savings("fake-savings-id")
    savings.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/savings/fake-savings-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_savings_rates(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"days": 30}
    savings.get_savings_rates(**test_data)
    savings.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/savings/rates",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_savings_returns(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"page_size": 20, "start_date": "2022-01-01", "end_date": "2022-12-28"}
    savings.get_savings_returns("fake_savings_id", **test_data)
    savings.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/savings/"
        f"fake_savings_id/returns?{savings._format_query(test_data)}",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_savings_performance(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"page_size": 20, "start_date": "2022-01-01", "end_date": "2022-12-28"}
    savings.get_savings_performance("fake_savings_id", **test_data)
    savings.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/savings/"
        f"fake_savings_id/performance?{savings._format_query(test_data)}",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_withdraw(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"savings_id": "test_savings_id", "amount": 5000}
    savings.withdraw(**test_data)
    savings.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/savings/"
        f"{test_data.pop('savings_id')}/withdraw",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_rollover(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"savings_id": "test_savings_id", "days": 30}
    savings.rollover(**test_data)
    savings.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/savings/"
        f"{test_data.pop('savings_id')}/rollover",
        json.dumps(test_data),
    )
