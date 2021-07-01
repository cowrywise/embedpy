from embed.resources.price import Price
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest
from tests.responses import json_responses



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_price_history(mock_get_essential_details, api_session):
    price = Price(api_session)
    mock_get_essential_details.return_value = MagicMock(data=json_responses.GET_PRICE_HISTORY_RESPONSE, status_code=200)
    test_data = {"asset_id": "fake-asset-id", "from_date": "2020-11-10", "to_date": "2020-11-12"}
    response = price.get_price_history(
        asset_id  = test_data.get("asset_id"),
        from_date = test_data.get("from_date"),
        to_date = test_data.get("to_date")
    )
    assert response.data == json_responses.GET_PRICE_HISTORY_RESPONSE and response.status_code == 200
    price.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/prices?asset_id=fake-asset-id&from_date=2020-11-10&to_date=2020-11-12",
    )