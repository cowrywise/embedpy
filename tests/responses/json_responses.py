import json

def get_api_json_responses(path):
    with open(path) as f:
        data = json.load(f)
    return data


#ACCOUNTS RESPONSES
CREATE_ACCOUNTS_RESPONSE = get_api_json_responses('tests/responses/create_account_200.json')
GET_ACCOUNTS_RESPONSE = get_api_json_responses('tests/responses/get_account_200.json')
GET_SINGLE_ACCOUNTS_RESPONSE = get_api_json_responses('tests/responses/get_single_account_200.json')
GET_PORTFOLIO_RESPONSE = get_api_json_responses('tests/responses/get_portfolio_200.json')
UPDATE_ADDRESS_RESPONSE = get_api_json_responses('tests/responses/update_address_200.json')
UPDATE_NOK_RESPONSE = get_api_json_responses('tests/responses/update_nok_200.json')
UPDATE_PROFILE_RESPONSE = get_api_json_responses('tests/responses/update_profile_200.json')
UPDATE_IDENTITY_RESPONSE = get_api_json_responses('tests/responses/update_identity_200.json')

#ASSETS RESPONSES
GET_ASSETS_RESPONSE = get_api_json_responses('tests/responses/get_assets_200.json')
MUTUAL_FUND_ASSET_RESPONSE = get_api_json_responses('tests/responses/mutual_fund_assets.json')
GET_SINGLE_ASSET_RESPONSE - get_api_json_responses('tests/responses/get_single_asset_200.json')
GET_INDEXES_RESPONSE = get_api_json_responses('tests/responses/get_indexes_200.json')
GET_INDEXED_ASSET_RESPONSE = get_api_json_responses('tests/responses/get_indexed_asset_200.json')

#AUTH RESPONSES
REFRESH_TOKEN_RESPONSE = get_api_json_responses('tests/responses/refresh_token_200.json')
FAILED_REFRESH_TOKEN_RESPONSE = get_api_json_responses('tests/responses/refresh_token_401.json')

#INVESTMENTS RESPONSES
GET_INVESTMENTS_RESPONSE = get_api_json_responses('tests/responses/get_investments_200.json')
GET_TBILLS_INVESTMENTS_RESPONSE = get_api_json_responses('tests/responses/get_tbills_investments_200.json')
CREATE_INVESTMENTS_RESPONSE = get_api_json_responses('tests/responses/create_investment_200.json')
LIQUIDATE_INVESTMENT_RESPONSE = get_api_json_responses('tests/responses/liquidate_investment_200.json')

#PRICES RESPONSES
GET_PRICE_HISTORY_RESPONSE = get_api_json_responses('tests/responses/get_price_history_200.json')

#SAVINGS RESPONSES
CREATE_SAVINGS_RESPONSE = get_api_json_responses('tests/responses/create_savings_response_200.json')
GET_SAVINGS_RESPONSE = get_api_json_responses('tests/responses/get_savings_response_200.json')

#STOCKS RESPONSES
GET_STOCKS_RESPONSE = get_api_json_responses('tests/responses/get_stocks_response_200.json')

#TRANSACTIONS RESPONSES
GET_TRANSACTIONS_RESPONSE = get_api_json_responses('tests/responses/get_transactions_response_200.json')
GET_LIMITED_TRANSACTIONS_RESPONSE = get_api_json_responses('tests/responses/limited_transactions_response_200.json')

#TRANSFERS RESPONSES
GET_TRANSFER_RESPONSE = get_api_json_responses('tests/responses/get_transfers_response_200.json')

#WALLETS RESPONSES
GET_WALLETS_RESPONSE = get_api_json_responses('tests/responses/get_wallets_response_200.json')
CREATE_WALLET_RESPONSE = get_api_json_responses('tests/responses/create_wallet_response_200.json')

ERROR_RESPONSE = get_api_json_responses('tests/responses/error_response_400_401.json')
