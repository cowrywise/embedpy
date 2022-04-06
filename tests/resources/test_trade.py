import json
from unittest.mock import MagicMock, patch

from embed.resources.trade import Trade


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_stocks(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_stocks()
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/assets",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_position(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_single_position(account_id="fake-id", stock_symbol="SYBL")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"SYBL/positions?account_id=fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_orders(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_orders(account_id="fake-id")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"orders?account_id=fake-id&status=open",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_profile(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_profile(account_id="fake-id")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"profile?account_id=fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_position(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_position(account_id="fake-id")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"positions?account_id=fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_buy_stock(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-id",
        "symbol": "sym",
        "amount": 200,
        "side": "side",
        "the_type": "type",
        "time_in_force": "tif",
        "idempotency_key": "test_idempotency_key",
    }
    trade.buy_stock(**test_data)
    idp_key = trade._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
    trade.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/buy",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_sell_stock(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake-id",
        "symbol": "sym",
        "amount": 200,
        "side": "side",
        "the_type": "type",
        "time_in_force": "tif",
        "idempotency_key": "test_idempotency_key",
    }
    trade.sell_stock(**test_data)
    idp_key = trade._headers.get("Embed-Idempotency-Key")
    assert test_data.pop("idempotency_key") == idp_key
    trade.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/sell",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_close_all_positions(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {"account_id": "fake-id"}
    trade.close_all_positions(account_id=test_data.get("account_id"))
    trade.get_essential_details.assert_called_with(
        "DELETE",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"positions?account_id=fake-id",
    )
