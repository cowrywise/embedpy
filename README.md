# Cowrywise Embed Python Library
The Embed Python library provides an easy access to the Embed Investment API by [Cowrywise](https://cowrywise.com/embed). Embed is an investment-as-a-service API that allows you to integrate investment features in your products and offer financial services to your customers at scale. With Embed, developers can create investment accounts for their customers and expose them to a wide variety of investment products!


## Documentation
See the [Embed API docs](developer.cowrywise.com).

## Installation
Clone the repo or install the library via pypi.

```
$ pip install embed-python (not yet)
```

### Requirements
- Python3+

## Usage
To get started, signup for developer credentials on [app.cowrywise.com](https://app.cowrywise.com). Once you signup, you can retrieve
you client_id and client_secret keys from the developer dashboard. Set your credentials in environment variables. 

```
# Environment variables
CLIENT_ID = CWRY-substitute-yours-here
CLIENT_SECRET = CWRY-SECRET-substitute-yours-here
```
Alternatively, you could use them to initialize the api client instance directly, after you import the APIClient.

```
from embed import APIClient
api_client = APIClient(client_id, client_secret)

# Get investment accounts associated with this credentials
api_client.accounts.get_accounts()

# Get all available assets to invest in
api_client.assets.get_assets()

# Get all available indexes to invest in
api_client.indexes.get_indexes()

# Get all investments made
api_client.investments.get_investments()
```







