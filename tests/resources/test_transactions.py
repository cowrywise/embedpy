from embed.resources.transaction import Transaction
from embed import errors
from unittest.mock import MagicMock, patch
import json
import pytest



@patch('embed.common.APIResponse.get_essential_details')
def test_can_get_transactions(mock_get_essential_details, api_session):
    transaction = Transaction(api_session)
    mock_get_essential_details.return_value = MagicMock()
    transaction.get_transactions()
    transaction.get_essential_details.assert_called_with(
        "GET",
        f"{api_session.base_url}/api/{api_session.api_version}/transactions",
    )