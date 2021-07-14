from embed.resources.saving import Saving
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_savings(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "days": "30",
        "interest_enabled": True,
        "currency_code": "NGN",
    }
    savings.create_savings(
        account_id=test_data.get("account_id"),
        days=test_data.get("days"),
        interest_enabled=test_data.get("interest_enabled"),
        currency_code=test_data.get("currency_code"),
    )
    savings.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/savings",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_savings(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-account-id",
        "days": "30",
        "interest_enabled": True,
        "currency_code": "NGN",
    }
    savings.create_savings(
        account_id=test_data.get("account_id"),
        days=test_data.get("days"),
        interest_enabled=test_data.get("interest_enabled"),
        currency_code=test_data.get("currency_code"),
    )
    savings.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/savings",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_savings(mock_get_essential_details, api_session):
    savings = Saving(api_session)
    mock_get_essential_details.return_value = MagicMock()
    savings.get_savings()
    savings.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/savings",
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
