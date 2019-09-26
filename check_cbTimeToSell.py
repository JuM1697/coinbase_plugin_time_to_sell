#!/usr/bin/python3

import sys,argparse
from coinbase.wallet.client import Client

parser = argparse.ArgumentParser(description='Get the current Price of Coinbase Cryptos')
parser.add_argument("-k", "--key", required=True, help="Coinbase API Key")
parser.add_argument("-s", "--secret", required=True, help="Coinbase API Secret")
parser.add_argument("-m", "--outcomeMethod", required=True, help="Desired Target Outcome Method e.g. EUR Wallet")
parser.add_argument("-c", "--currencyToSell", required=True, help="Desired Target Currency to sell e.g. BTC")
parser.add_argument("-a", "--accountWallet", required=True, help="Desired Target wallet to sell from e.g. BTC Wallet")
parser.add_argument("-o", "--outcome", required=True, help="Desired amount to receive from Outcome Method e.g. 5.00")
parser.add_argument("-t", "--trade", required=True, help="How much of the desired Crypto would you like to sell (trade) for the previously defined amount to receive? e.g. 23")
args = vars(parser.parse_args())


api_key = args["key"]
api_secret = args["secret"]
targetOutcomeMethod = args["outcomeMethod"]
targetCurrency = args["currencyToSell"]
targetSellCurrencyWallet = args["accountWallet"]
receiveMoneyWish = float(args["outcome"])
targetAmountToSell = args["trade"]

# Create Connection Client client
client = Client(api_key, api_secret)

# Get all payment methods and accounts
accounts = client.get_accounts()
pms = client.get_payment_methods()

for method in pms.data:
    if method['name'] == targetOutcomeMethod:
        paymentID = method['id']

for account in accounts.data:
    if account['name'] == targetSellCurrencyWallet:
        accountID = account['id']

# Creating the sell order the arguments quote and commit are used to create only a preview
# Order can not be executed this way
# The current outcome you would receive is stored to outcome variable
sell = client.sell(accountID,commit="false",amount=targetAmountToSell, currency=targetCurrency, payment_method=paymentID, quote="true")
outcome = float(sell["total"]["amount"])

# Last but not least:
# Comparing the sell reward with the desired sell reward.
# CRITICAL if desired reward (outcome) is reached
# OK if its not reached yet
if outcome > receiveMoneyWish:
    print("Your desired target outcome is reached! Time to sell! | outcome="+str(outcome))
    sys.exit(2)
else:
    print("Your desired target outcome is not reached yet. Keep waiting! | outcome="+str(outcome))
    sys.exit(0)
