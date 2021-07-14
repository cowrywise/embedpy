from embed.resources.account import Account
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_account(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"first_name": "test", "last_name": "tester", "email": "tester@abc.com"}
    account.create_account(
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        email=test_data.get("email"),
    )
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_create_account_with_zero_params_raises_validation_error(
    mock_get_essential_details, api_session
):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    with pytest.raises(errors.ValidationError):
        account.create_account()


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_accounts(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    account.get_accounts()
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_account(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    account.get_account("id")
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_portfolio(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    account.get_portfolio("fake_id")
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/portfolio",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_update_address(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake_id",
        "street": "Broadway",
        "lga": "Eti-Osa",
        "area_code": "100034",
        "city": "Lagos",
        "state": "Lagos",
        "country": "NG",
    }
    account.update_address(
        account_id=test_data.get("account_id"),
        street=test_data.get("street"),
        lga=test_data.get("lga"),
        area_code=test_data.get("area_code"),
        city=test_data.get("city"),
        state=test_data.get("state"),
        country=test_data.get("country"),
    )
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/address",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_update_next_of_kin(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake_id",
        "email": "jd@gmail.com",
        "first_name": "John",
        "last_name": "Doe",
        "phone_number": "+2348034031863",
        "relationship": "Friend",
        "gender": "M",
    }
    account.update_next_of_kin(
        account_id=test_data.get("account_id"),
        email=test_data.get("email"),
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        phone_number=test_data.get("phone_number"),
        relationship=test_data.get("relationship"),
        gender=test_data.get("gender"),
    )
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/nok",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_update_profile(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake_id",
        "first_name": "Uchechukwu",
        "last_name": "Emmanuel",
        "email": "darlington@abc.com",
        "gender": "M",
        "phone_number": "+2349054314310",
        "date_of_birth": "1959-10-10",
    }
    account.update_profile(
        account_id=test_data.get("account_id"),
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        email=test_data.get("email"),
        gender=test_data.get("gender"),
        phone_number=test_data.get("phone_number"),
        date_of_birth=test_data.get("date_of_birth"),
    )
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/profile",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_update_identity(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake_id",
        "identity_type": "bvn",
        "identity_value": "0123456789",
    }
    account.update_identity(
        account_id=test_data.get("account_id"),
        identity_type=test_data.get("identity_type"),
        identity_value=test_data.get("identity_value"),
    )
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/identity",
        json.dumps(test_data),
    )
