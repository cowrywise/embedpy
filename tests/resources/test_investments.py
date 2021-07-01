from embed.resources.investment import Investment
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest
from tests.responses import json_responses



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_investments(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_INVESTMENTS_RESPONSE, status_code=200)
    response = investment.get_investments()
    assert response.data == json_responses.GET_INVESTMENTS_RESPONSE and response.status_code == 200
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_single_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_INVESTMENTS_RESPONSE, status_code=200)
    response = investment.get_investment("fake-investment-id")
    assert response.data == json_responses.GET_INVESTMENTS_RESPONSE and response.status_code == 200
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/fake-investment-id",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_filtered_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_SINGLE_INVESTMENT_RESPONSE, status_code=200)
    response = investment.get_filtered_investments("tbills")
    assert response.data == json_responses.GET_SINGLE_INVESTMENT_RESPONSE and response.status_code == 200
    investment.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/investments?asset_type=tbills",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_create_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.CREATE_INVESTMENTS_RESPONSE, status_code=200)
    test_data = {'account_id': 'bbaaaaaabbb6477f866b20161e003ebb', 'asset_code': 'AST-TBILL-0001000000'}
    response = investment.create_investment(account_id=test_data.get('account_id'), asset_code=test_data.get('asset_code'))
    assert response.data == json_responses.CREATE_INVESTMENTS_RESPONSE and response.status_code == 200
    investment.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/investments",
        json.dumps(test_data)
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_liquidate_investment(mock_get_essential_details, api_session):
    investment = Investment(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.LIQUIDATE_INVESTMENT_RESPONSE, status_code=200)
    test_data = {'investment_id': 'fake-investment-id', 'units': '200'}
    response = investment.liquidate_investment(
                investment_id=test_data.get('investment_id'),
                units=test_data.get('units')
            )
    assert response.data == json_responses.LIQUIDATE_INVESTMENT_RESPONSE and response.status_code == 200
    investment.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/investments/fake-investment-id/liquidate",
        json.dumps({'units': '200'})
    )