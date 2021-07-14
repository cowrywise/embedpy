from embed.resources.price import Price
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_price_history(mock_get_essential_details, api_session):
    price = Price(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "asset_id": "fake-asset-id",
        "from_date": "2020-11-10",
        "to_date": "2020-11-12",
    }
    price.get_price_history(
        asset_id=test_data.get("asset_id"),
        from_date=test_data.get("from_date"),
        to_date=test_data.get("to_date"),
    )
    price.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/prices?asset_id=fake-asset-id&from_date=2020-11-10&to_date=2020-11-12",
    )
