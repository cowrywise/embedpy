import json
from unittest.mock import patch, MagicMock

from embed.resources.stock_portfolio import StockPortfolio


@patch("embed.common.APIResponse.get_essential_details")
def test_can_list_stock_portfolio(mock_get_essential_details, api_session):
    stock_portfolio = StockPortfolio(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock_portfolio.list_stock_portfolio(page_size=20)
    stock_portfolio.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks-portfolio?page_size=20",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_get_stock_portfolio(mock_get_essential_details, api_session):
    stock_portfolio = StockPortfolio(api_session)
    mock_get_essential_details.return_value = MagicMock()
    stock_portfolio.get_stock_portfolio("fake_portfolio_id")
    stock_portfolio.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks-portfolio/fake_portfolio_id",
    )


@patch("embed.common.APIResponse.get_essential_details")
def test_can_create_stock_portfolio(mock_get_essential_details, api_session):
    stock_portfolio = StockPortfolio(api_session)
    mock_get_essential_details.return_value = MagicMock()
    test_data = {
        "account_id": "fake_id",
        "risk_class": "GROW",
        "investment_preference": "MINIMIZE_LOSSES",
    }
    stock_portfolio.create_stock_portfolio(**test_data)
    stock_portfolio.get_essential_details.assert_called_with(
        "POST",
        f"{api_session.base_url}/api/{api_session.api_version}/stocks-portfolio",
        json.dumps(test_data),
    )
