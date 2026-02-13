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

### Initialization

```python
from embed.client import Client

# Initialize with environment variables (CLIENT_ID, CLIENT_SECRET)
client = Client()

# Or initialize with explicit credentials
client = Client(
    client_id='your_client_id',
    client_secret='your_client_secret',
    base_url="https://sandbox.cowrywise.com"  # Optional
)
```

### Example: Creating an Account and Investment

```python
# 1. Create a user account
account = client.account.create_account(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    terms_of_use_accepted=True
)
account_id = account['data']['account_id']

# 2. List available assets
assets = client.asset.list_assets(asset_type="tbills")

# 3. Create an investment
investment = client.investment.create_investment(
    account_id=account_id,
    asset_code="AST-TBILL-0001",
    amount=10000.0
)
```

## Embed API REST Methods

| Rest Method                                                      | Endpoint          |
|------------------------------------------------------------------|-------------------|
| `create_account(first_name=None, last_name=None, email=None, **kwargs)` | `POST /accounts`    |
| `get_account(account_id)`                                          | `GET /accounts/:id` |
| `update_next_of_kin(account_id, email, first_name, last_name, phone_number, relationship, gender)` | `POST /accounts/:id/nok` |
| `get_portfolio(account_id)`                                        | `GET /accounts/:id/portfolio` |
| `get_asset(asset_id)`                                        | `GET /assets/:id/` |
| `list_assets(country=None, asset_type=None)`                 | `GET /assets?country=None&asset_type=None` |
| `get_index(index_id)`                 | `GET /indexes/:id` |
| `create_custom_index(account_id=None, name=None, description=None, allocations=None)` | `POST /indexes` |
| `modify_custom_index(account_id=None, index_id=None, allocations=None)`  | `PUT /indexes/:index_id` |
| `get_investment(investment_id)`  | `GET /investments/:id` |
| `create_investment(account_id=None, asset_code=None, **kwargs)`  | `POST /investments` |
| `liquidate_investment(investment_id=None, units=None, **kwargs)`  | `POST /investments/:id/liquidate` |
| `get_price_history(asset_id=None, from_date=None, to_date=None)`  | `GET /prices?asset_id=None&from_date=None&to_date=None` |
| `create_savings(account_id=None, days=None, interest_enabled=None, currency_code=None)`  | `POST /savings` |
| `buy_stock(account_id=None, symbol=None, amount=None, side=None, the_type=None, time_in_force=None)`  | `POST /stocks/buy` |
| `sell_stock(account_id=None, symbol=None, amount=None, side=None, the_type=None, time_in_force=None)`  | `POST /stocks/sell` |
| `list_transfers(account_id=None, email=None, from_date=None, to_date=None)`  | `GET /transfers/:id?email=None&from_date=None&to_date=None` |
| `get_deposit(deposit_id)`  | `GET /deposits/:id` |
| `create_wallet(account_id=None, currency_code=None)`  | `POST /wallets` |
| `transfer(wallet_id=None, product_code=None, amount=None)`  | `POST /wallets/:wallet_id/transfer` |
| `get_wallet(wallet_id)`  | `GET /wallets/:wallet_id` |
| `list_flexible_savings(**kwargs)` | `GET /flexible-savings` |
| `create_fixed_note(**kwargs)` | `POST /fixed-notes` |
| `list_eurobonds(**kwargs)` | `GET /eurobonds` |
| `list_fixed_placements(**kwargs)` | `GET /fixed-placements` |
| `list_withdrawals(**kwargs)` | `GET /withdrawals` |
| `cscs_onboarding(**kwargs)` | `POST /integration/cscs/onboarding` |
| `atomic_onboarding(**kwargs)` | `POST /integration/atomic/onboarding` |

Check the [API reference](https://developers.cowrywise.com/reference) document for all resources and their respective endpoints.

# Contributions

We welcome contributions from everyone. Before submitting a pull request, kindly ensure:

- [ ] Necessary tests for the code changes requested are added
- [ ] Code is formatted according to PEP8
- [ ] There is clear commit messages
