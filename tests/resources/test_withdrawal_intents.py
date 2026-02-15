import json
from embed.resources.withdrawal_intents import WithdrawalIntent
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_withdrawal_intent(mock_get_essential_details, api_session):
    wi = WithdrawalIntent(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "bank_id": "fake-bank-id",
        "amount": 5000,
        "currency": "NGN",
    }
    wi.create_withdrawal_intent(**test_data)
    wi.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawal-intents",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_withdrawal_intents(mock_get_essential_details, api_session):
    wi = WithdrawalIntent(api_session)
    mock_get_essential_details.return_value = MagicMock()
    wi.list_withdrawal_intents(currency="NGN")
    wi.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawal-intents?currency=NGN",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_retry_withdrawal_intent(mock_get_essential_details, api_session):
    wi = WithdrawalIntent(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "reference": "fake-ref",
        "currency": "NGN",
    }
    wi.retry_withdrawal_intent(**test_data)
    wi.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawal-intents/retry",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_cancel_withdrawal_intent(mock_get_essential_details, api_session):
    wi = WithdrawalIntent(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "reference": "fake-ref",
        "currency": "NGN",
    }
    wi.cancel_withdrawal_intent(**test_data)
    wi.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/withdrawal-intents/cancel",
        json.dumps(test_data),
    )
