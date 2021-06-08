import pytest
from embed.client import Client

# @pytest.mark.parametrize(
#     "resource_name",
#     [
#         "Accounts",
#         "Links",
#         "Transactions",
#         "Balances",
#         "Owners",
#         "Institutions",
#         "Incomes",
#         "Invoices",
#         "TaxReturns",
#         "Statements",
#         "WidgetToken",
#     ],
# )
# def test_client_resources_uses_same_session_as_client(resource_name):
#     c = Client(client_id="a", client_secret="b")
#     assert c.session is getattr(c, resource_name).session
