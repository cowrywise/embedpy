import json
from embed.resources.fixed_notes import FixedNote
from unittest.mock import MagicMock, patch


@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_fixed_notes(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fn.list_fixed_notes(page_size=20)
    fn.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_fixed_note(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fn.get_fixed_note("fake-fn-id")
    fn.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes/fake-fn-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_fixed_note(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "asset_code": "FN-ASSET",
        "tenor_in_months": 12,
        "amount_range": "10k-100k",
        "idempotency_key": "test-key",
    }
    fn.create_fixed_note(**test_data)
    fn.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes",
        json.dumps(
            {
                "account_id": "fake-account-id",
                "asset_code": "FN-ASSET",
                "tenor_in_months": 12,
                "amount_range": "10k-100k",
            }
        ),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_fixed_note_rates(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fn.get_fixed_note_rates(tenor_in_months=6, amount_range="10k-100k", currency="NGN")
    fn.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes/rates?tenor_in_months=6&amount_range=10k-100k&currency=NGN",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_withdraw_from_fixed_note(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fn.withdraw("fake-fn-id", amount=5000)
    fn.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes/fake-fn-id/withdraw",
        json.dumps({"amount": 5000}),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_rollover_fixed_note(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fn.rollover("fake-fn-id", tenor_in_months=3)
    fn.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes/fake-fn-id/rollover",
        json.dumps({"tenor_in_months": 3}),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_partial_update(mock_get_essential_details, api_session):
    fn = FixedNote(api_session)
    mock_get_essential_details.return_value = MagicMock()
    fn.partial_update("fake-fn-id", auto_reinvest=True)
    fn.get_essential_details.assert_called_with(
        "PATCH",
        f"{api_session.base_url}/api/{api_session.api_version}/fixed-notes/fake-fn-id",
        json.dumps({"auto_reinvest": True}),
    )
