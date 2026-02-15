import json
from embed.resources.flexible_savings import FlexibleSaving
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_flexible_savings(mock_get_essential_details, api_session):
    fs = FlexibleSaving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fs.list_flexible_savings(page_size=20)
    fs.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/flexible-savings?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_flexible_savings(mock_get_essential_details, api_session):
    fs = FlexibleSaving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fs.get_flexible_savings("fake-fs-id")
    fs.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/flexible-savings/fake-fs-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_flexible_savings(mock_get_essential_details, api_session):
    fs = FlexibleSaving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "currency_code": "NGN",
        "idempotency_key": "test_id_key",
    }
    fs.create_flexible_savings(**test_data)
    fs.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/flexible-savings",
        json.dumps({"account_id": "fake-account-id", "currency_code": "NGN"}),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_flexible_savings_rates(mock_get_essential_details, api_session):
    fs = FlexibleSaving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fs.get_flexible_savings_rates()
    fs.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/flexible-savings/rates",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_flexible_savings_performance(mock_get_essential_details, api_session):
    fs = FlexibleSaving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fs.get_flexible_savings_performance("fake-fs-id", start_date="2023-01-01")
    fs.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/flexible-savings/fake-fs-id/performance?start_date=2023-01-01",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_withdraw_from_flexible_savings(mock_get_essential_details, api_session):
    fs = FlexibleSaving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fs.withdraw("fake-fs-id", amount=1000)
    fs.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/flexible-savings/fake-fs-id/withdraw",
        json.dumps({"amount": 1000}),
    )
