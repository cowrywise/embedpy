from embed.resources.account import Account
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest
from tests.responses import json_responses



@patch('embed.common.APIResponse.get_essential_details')
def test_can_create_account(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.CREATE_ACCOUNTS_RESPONSE, status_code=200)
    test_data = {"first_name": "test", "last_name": "tester", "email": "tester@abc.com"}
    response = account.create_account(
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        email=test_data.get("email"),
    )
    assert response.data == json_responses.CREATE_ACCOUNTS_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts",
        json.dumps(test_data),
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_create_account_with_zero_params_raises_validation_error(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.ERROR_RESPONSE, status_code=400)
    with pytest.raises(errors.ValidationError):
        account.create_account()


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_accounts(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_ACCOUNTS_RESPONSE, status_code=200)
    response = account.get_accounts()
    assert response.data == json_responses.GET_ACCOUNTS_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_single_account(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_SINGLE_ACCOUNTS_RESPONSE, status_code=200)
    response = account.get_account("id")
    assert response.data == json_responses.GET_SINGLE_ACCOUNTS_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/id",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_portfolio(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_PORTFOLIO_RESPONSE,
                                                        status_code=200)
    response = account.get_portfolio("fake_id")
    assert response.data == json_responses.GET_PORTFOLIO_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/portfolio",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_update_address(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.UPDATE_ADDRESS_RESPONSE, status_code=200)
    test_data = {"account_id": "fake_id", "street": "Broadway", "lga": "Eti-Osa", "area_code": "100034", "city": "Lagos", "state": "Lagos", "country": "NG"}
    response = account.update_address(
        account_id=test_data.get("account_id"),
        street=test_data.get("street"),
        lga=test_data.get("lga"),
        area_code=test_data.get("area_code"),
        city=test_data.get("city"),
        state=test_data.get("state"),
        country=test_data.get("country")
    )
    assert response.data == json_responses.UPDATE_ADDRESS_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/address",
        json.dumps(test_data),
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_update_next_of_kin(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.UPDATE_NOK_RESPONSE, status_code=200)
    test_data = {'account_id':'fake_id', 'email': 'jd@gmail.com', 'first_name': 'John', 'last_name': 'Doe', 'phone_number': '+2348034031863', 'relationship': 'Friend', 'gender': 'M'}
    response = account.update_next_of_kin(
        account_id=test_data.get("account_id"),
        email=test_data.get("email"),
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        phone_number=test_data.get("phone_number"),
        relationship=test_data.get("relationship"),
        gender=test_data.get("gender")
    )
    assert response.data == json_responses.UPDATE_NOK_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/nok",
        json.dumps(test_data),
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_update_profile(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.UPDATE_PROFILE_RESPONSE, status_code=200)
    test_data = { 'account_id': 'fake_id', 'first_name': 'Uchechukwu', 'last_name': 'Emmanuel', 'email': 'darlington@abc.com', 'gender': 'M', 'phone_number': '+2349054314310', 'date_of_birth': '1959-10-10' }
    response = account.update_profile(
        account_id=test_data.get("account_id"),
        first_name=test_data.get("first_name"),
        last_name=test_data.get("last_name"),
        email=test_data.get("email"),
        gender=test_data.get("gender"),
        phone_number=test_data.get("phone_number"),
        date_of_birth=test_data.get("date_of_birth"),

    )
    assert response.data == json_responses.UPDATE_PROFILE_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/profile",
        json.dumps(test_data),
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_update_identity(mock_get_essential_details, api_session):
    account = Account(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.UPDATE_IDENTITY_RESPONSE, status_code=200)
    test_data = { 'account_id': 'fake_id', 'identity_type': 'bvn', 'identity_value': '0123456789' }
    response = account.update_identity(
        account_id=test_data.get("account_id"),
        identity_type=test_data.get("identity_type"),
        identity_value=test_data.get("identity_value"),
    )
    assert response.data == json_responses.UPDATE_IDENTITY_RESPONSE and response.status_code == 200
    account.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/accounts/fake_id/identity",
        json.dumps(test_data),
    )