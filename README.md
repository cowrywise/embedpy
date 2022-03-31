# Embed Python Library

The Embed Python library provides an easy access to the Embed Investment API by [Cowrywise](https://cowrywise.com/embed). Embed is an investment-as-a-service API that allows you to integrate investment features in your products and offer financial services to your customers at scale. With Embed, developers can create investment accounts for their customers and expose them to a wide variety of investment products!

## Documentation

See the [Embed API docs](https://developers.cowrywise.com).

## Installation

Install the package directly via git

```python
pip install git+https://github.com/cowrywise/embedpy.git
```

You could also install the library via pypi using the pip package manager.

```python
$ pip install -U embedpy
```

### Requirements

- Python3+

## Usage

To get started, sign up for your developer credentials on the [Embed Dashboard](https://embed.cowrywise.com). Once you have signed up, you can retrieve your `client_id` and `client_secret` keys from the developer dashboard. Set your credentials in the environment variables before creating an instance of the Embed Client.

```python
# Set environment variables
CLIENT_ID = CWRY-substitute-yours-here
CLIENT_SECRET = CWRY-SECRET-substitute-yours-here

# Create an instance of the Embed Client
from embed.client import Client
client = Client()
```

Alternatively, you can use your credentials to instantiate the Embed Client. During this instantiation, you can specify a base URL. This is an optional parameter that defaults to the sandbox base URL.

```python
from embed.client import Client
client = Client(client_id='****', client_secret='****', base_url="https://***.cowrywise.com")
```

## Embed API REST Methods

| Rest Method                                                      | Endpoint          |
|------------------------------------------------------------------|-------------------|
| create_account(first_name=None, last_name=None, email=None)      | `POST /accounts`    |
| get_account(account_id)                                          | `GET /accounts/:id` |
| update_next_of_kin(account_id=None, email=None, first_name=None,/last_name=None, phone_number=None, relationship=None, gender=None) | `POST /accounts/:id/nok` |
| get_portfolio(account_id)                                        | `GET /accounts/:id/portfolio` |
| get_asset(asset_id)                                        | `GET /assets/:id/` |
| list_assets(country=None, asset_type=None)                 | `GET /assets?country=None&asset_type=None` |
| get_index(index_id)                 | `GET /indexes/:id` |
| create_custom_index(account_id=None, name=None, description=None, allocations=None) | `POST /indexes` |
| modify_custom_index(account_id=None, index_id=None, allocations=None)  | `PUT /indexes/:index_id` |
| get_investment(investment_id)  | `GET /investments/:id` |
| create_investment(account_id=None, asset_code=None)  | `POST /investments` |
| liquidate_investment(investment_id=None, units=None)  | `POST /investments/:id` |
| get_price_history(asset_id=None, from_date=None, to_date=None)  | `GET /prices?asset_id=None&from_date=None&to_date=None` |
| create_savings(account_id=None, days=None, interest_enabled=None, currency_code=None)  | `POST /savings` |
| buy_stock(account_id=None, symbol=None, amount=None, side=None, the_type=None, time_in_force=None)  | `POST /stocks/buy` |
| sell_stock(account_id=None, symbol=None, amount=None, side=None, the_type=None, time_in_force=None)  | `POST /stocks/sell` |
| list_transfers(account_id=None, email=None, from_date=None, to_date=None)  | `GET /transfers/:id?email=None&from_date=None&to_date=None` |
| get_deposit(deposit_id)  | `GET /deposits/:id` |
| create_wallet(account_id=None, currency_code=None)  | `POST /wallets` |
| transfer(wallet_id=None, product_code=None, amount=None)  | `POST /wallets/:wallet_id/transfer` |
| get_wallet(wallet_id)  | `GET /wallets/:wallet_id` |

Check the [API reference](https://developers.cowrywise.com/reference) document for all resources and their respective endpoints.

# Contributions

We welcome contributions from everyone. Before submitting a pull request, kindly ensure:

- [ ] Necessary tests for the code changes requested are added
- [ ] Code is formatted according to PEP8
- [ ] There is clear commit messages
