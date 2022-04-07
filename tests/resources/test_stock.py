import json
from unittest.mock import patch, MagicMock

from embed.resources.stock import Stock


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_stocks(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock.list_stocks(page_size=20)
    stock.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"assets?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_single_stock_asset(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock.get_stocks(symbols=["fake_symbol_1", "fake_symbol_2"], page_size=20)
    stock.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"assets?symbol=fake_symbol_1&symbol=fake_symbol_2&page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_buy_stocks(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "test_account_id",
        "symbol": "test_symbol",
        "amount": 5000,
        "side": "buy",
        "type": "market",
        "time_in_force": "day",
    }
    stock.buy_stocks(**test_data)
    stock.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/buy",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_sell_stocks(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "test_account_id",
        "symbol": "test_symbol",
        "amount": 5000,
        "side": "sell",
        "type": "market",
        "time_in_force": "day",
    }
    stock.sell_stocks(**test_data)
    stock.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/sell",
        json.dumps(test_data),
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_profile(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock.get_profile("fake_id")
    stock.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"profile?account_id=fake_id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_positions(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock.get_positions("fake_id")
    stock.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"positions?account_id=fake_id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_position(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock.get_position("fake_id", "fake_symbol")
    stock.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"positions/fake_symbol?account_id=fake_id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_orders(mock_get_essential_details, api_session):
    stock = Stock(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock.get_orders("fake_id", "fake_status")
    stock.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks/"
        f"orders?account_id=fake_id&status=fake_status",
    )
