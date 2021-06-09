# Embed Python Library
The Embed Python library provides an easy access to the Embed Investment API by [Cowrywise](https://cowrywise.com/embed). Embed is an investment-as-a-service API that allows you to integrate investment features in your products and offer financial services to your customers at scale. With Embed, developers can create investment accounts for their customers and expose them to a wide variety of investment products!


## Documentation
See the [Embed API docs](developer.cowrywise.com).

## Installation
Clone the repo or install the library via pypi.

```python
$ pip install embed-python (not yet)
```

### Requirements
- Python3.8+

## Usage
To get started, signup for developer credentials on [app.cowrywise.com](https://app.cowrywise.com). Once you signup, you can retrieve
you client_id and client_secret keys from the developer dashboard. Set your credentials in environment variables. 

```python
# Set environment variables
CLIENT_ID = CWRY-substitute-yours-here
CLIENT_SECRET = CWRY-SECRET-substitute-yours-here

# Create an instance of the Embed Client
from embed import Client
client = Client()
```

Alternatively, initialize the Embed Client with your credentials.

```python
from embed import Client
client = Client(client_id='****', client_secret='****')
```
#### Create Accounts
```python
# Create investment account for your customer
client.accounts.create_account(
   first_name= "Mansa",
   last_name= "Musa",
   email= "mans_not_hot@gmaili.com
)
```
#### Create Investments
```python
# You can invest in Assets (Mutual funds, Tbills, Stocks) or Indexes
# Get all available assets to invest in
client.assets.get_assets()

# Create an investment with a given asset code
client.investments.create_investment(
  account_id="8ddfb5ea9fe440f9a7d086b7c8f14abd",
  asset_code="AST-FUND-1655862279",
)
```
#### Transfer funds
```python
# Transfer funds from a wallet to a savings/investment product
client.transfers.initiate_transfer(
  source_wallet_id='ec45bb798f244c75b9432ec19256316b', 
  destination_product_code='PRCDE1297453250', 
  amount=50000, #kobo/cents 
  currency_code='NGN'
})
```
Check the [API reference](developers.cowrywise.com) document for more examples.

# Contributing
We welcome contribution from everyone. Before submitting a pull request, kindly ensure:
- [ ] Necessary tests for the code changes requested are added
- [ ]  Code is formatted according to PEP3
- [ ] There is clear commit messages







