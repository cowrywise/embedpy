# Cowrywise Embed Python Library
The Embed Python library provides an easy access to the Embed Investment API by Cowrywise. Embed is an investment-as-a-service API that allows you to integrate investment features in your products and offer financial services to your customers at scale. With Embed, developers can create investment accounts for their customers and expose them to a wide variety of investment products!


# Documentation
Read the API documentation.

# Installation
Clone the repo or install the library via pypi.

```
$ pip install embed-python
```

# Usage
To get started, signup for developer credentials on app.cowrywise.com. Once you signup, you can retrieve
you client_id and client_secret keys from the developer dashboard.

```
from embed import APIClient
api_client = APIClient(client_id, client_secret)

# Get Accounts: Get accounts associated with this credentials
api_client.accounts.get_accounts()

# Get Assets: Get all available assets to invest in
api_client.assets.get_assets()

# Get Investments: Get all investments made
api_client.investments.get_investments()

```




