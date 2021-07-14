from embed.resources.trade import Trade
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest


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
def test_can_get_stocks(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_single_position(account_id="fake-id", stock_symbol="SYBL")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/SYBL/positions?account_id=fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_orders(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_orders(account_id="fake-id")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/orders?account_id=fake-id&status=open",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_profile(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_profile(account_id="fake-id")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/profile?account_id=fake-id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_position(mock_get_essential_details, api_session):
    trade = Trade(api_session)
    mock_get_essential_details.return_value = MagicMock()
    trade.get_position(account_id="fake-id")
    trade.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/positions?account_id=fake-id",
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
    }
    trade.buy_stock(
        account_id=test_data.get("account_id"),
        symbol=test_data.get("symbol"),
        amount=test_data.get("amount"),
        side=test_data.get("side"),
        the_type=test_data.get("the_type"),
        time_in_force=test_data.get("time_in_force"),
    )
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
    }
    trade.sell_stock(
        account_id=test_data.get("account_id"),
        symbol=test_data.get("symbol"),
        amount=test_data.get("amount"),
        side=test_data.get("side"),
        the_type=test_data.get("the_type"),
        time_in_force=test_data.get("time_in_force"),
    )
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
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/positions?account_id=fake-id",
    )
