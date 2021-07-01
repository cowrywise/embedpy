from embed.resources.index import Index
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest
from tests.responses import json_responses



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_indexes(mock_get_essential_details, api_session):
    index = Index(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_INDEXES_RESPONSE, status_code=200)
    response = index.get_indexes()
    assert response.data == json_responses.GET_INDEXES_RESPONSE and response.status_code == 200
    index.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/indexes",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_index_assets(mock_get_essential_details, api_session):
    index = Index(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_INDEX_ASSETS_RESPONSE, status_code=200)
    response = index.get_index_assets("fake-asset-id")
    assert response.data == json_responses.GET_INDEX_ASSETS_RESPONSE and response.status_code == 200
    index.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/indexes/fake-asset-id/assets",
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_create_custom_index(mock_get_essential_details, api_session):
    index = Index(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.CREATE_CUSTOM_INDEX_RESPONSE, status_code=200)
    test_data = {
            "account_id":"88363e3c38ee4007b83c503cdb912fe0",
            "name":"Dewcs",
            "description":"A custom index containing x y z assets",
            "allocations": [
                    {
                        "asset_code": "AST-FUND-174669468",
                        "weight": 50
                    },
                    {
                        "asset_code": "AST-FUND-367626263",
                        "weight": 50
                    }
                        ]
            }
    response = index.create_custom_index(
        account_id=test_data.get("account_id"),
        name=test_data.get("name"),
        description=test_data.get("description"),
        allocations=test_data.get("allocations")
    )
    assert response.data == json_responses.CREATE_CUSTOM_INDEX_RESPONSE and response.status_code == 200
    index.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/indexes",
        json.dumps(test_data)
    )


@patch('embed.common.APIResponse.get_essential_details')
def test_can_modify_custom_index(mock_get_essential_details, api_session):
    index = Index(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.UPDATE_CUSTOM_INDEX_RESPONSE, status_code=200)
    test_data = {
            "account_id":"13d14443490b4e7baa44666c4d9acd35",
            "index_id": "fake-index-id",
            "allocations": [
                {
                    "asset_code": "AST-FUND-1711322920",
                    "weight": 0
                },
                {
                    "asset_code": "AST-FUND-35452689",
                    "weight": 30
                },
                {
                    "asset_code": "AST-TBILL-337839040",
                    "weight": 70
                }
                ]
            }
    response = index.modify_custom_index(
        account_id=test_data.get("account_id"),
        index_id= test_data.get("index_id"),
        allocations=test_data.get("allocations")
    )
    assert response.data == json_responses.UPDATE_CUSTOM_INDEX_RESPONSE and response.status_code == 200
    index.get_essential_details.assert_called_with(
        "PUT",
        f"{api_session.base_url}/api/{api_session.api_version}/indexes/fake-index-id",
        json.dumps(test_data)
    )