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
$ pip install embedpy
```

### Requirements

- Python3+

## Usage

To get started, signup for developer credentials on [Embed Dashboard](https://embed.cowrywise.com). Once you signup, you can retrieve
you client_id and client_secret keys from the developer dashboard. Set your credentials in environment variables.

```python
# Set environment variables
CLIENT_ID = CWRY-substitute-yours-here
CLIENT_SECRET = CWRY-SECRET-substitute-yours-here

# Create an instance of the Embed Client
from embed.client import Client
client = Client()
```

Alternatively, instantiate the Embed Client with your credentials. You can specify a base url during this instantiation. This is optional and defaults to the sandbox base url.

```python
from embed.client import Client
client = Client(client_id='****', client_secret='****', base_url="https://***.cowrywise.com")
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
client.assets.get_assets() or client.indexes.get_indexes()

# Create an investment with a given asset code
client.investments.create_investment(
  account_id="8ddfb5ea9fe440f9a7d086b7c8f14abd",
  asset_code="AST-FUND-1655862279",
)
```

#### Transfer funds

```python
# Transfer funds from a wallet to a savings/investments with product code
client.wallets.transfer(
  wallet_id='ec45bb798f244c75b9432ec19256316b',
  product_code='PRCDE1297453250',
  amount=50000, #kobo/cents
})
```

Check the [API reference](https://developers.cowrywise.com/reference) document for more examples.

# Contributions

We welcome contributions from everyone. Before submitting a pull request, kindly ensure:

- [ ] Necessary tests for the code changes requested are added
- [ ] Code is formatted according to PEP8
- [ ] There is clear commit messages
