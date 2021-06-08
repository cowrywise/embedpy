# Embed Python Library
The Embed Python library provides an easy access to the Embed Investment API by [Cowrywise](https://cowrywise.com/embed). Embed is an investment-as-a-service API that allows you to integrate investment features in your products and offer financial services to your customers at scale. With Embed, developers can create investment accounts for their customers and expose them to a wide variety of investment products!


## Documentation
See the [Embed API docs](developer.cowrywise.com).

## Installation
Clone the repo or install the library via pypi.

```
$ pip install embed-python (not yet)
```

### Requirements
- Python3.8+

## Usage
To get started, signup for developer credentials on [app.cowrywise.com](https://app.cowrywise.com). Once you signup, you can retrieve
you client_id and client_secret keys from the developer dashboard. Set your credentials in environment variables. 

```
# Set environment variables
CLIENT_ID = CWRY-substitute-yours-here
CLIENT_SECRET = CWRY-SECRET-substitute-yours-here

# Create an instance of the Embed Client
from embed import Client
client = Client()
```

Alternatively, initialize the Embed Client with your credentials.

```
from embed import Client
client = Client(client_id='****', client_secret='****')
```
### Create Investment Accounts
```
# Create investment account for your customer
client.accounts.create_account(
   first_name= "Mansa",
   last_name= "Musa",
   email= "mans_not_hot@gmaili.com
)
```
```
# You can invest in Assets (Mutual funds, Tbills, Stocks) or Indexes
# Get all available assets to invest in
client.assets.get_assets()

# Make an invest for your customer
client.investments.create_investment(
  account_id="8ddfb5ea9fe440f9a7d086b7c8f14abd",
  amount=50000, #kobo
  asset_code="AST-FUND-1655862279",
)
```

```
# Get a user's investment portfolio
client.accounts.get_portfolio('8ddfb5ea9fe440f9a7d086b7c8f14abd')
```

# Contributing
We welcome contribution from everyone. Before submitting a pull request, kindly ensure:
- [ ] Necessary tests for the code changes requested are added
- [ ]  Code is formatted according to PEP3
- [ ] There is clear commit messages







