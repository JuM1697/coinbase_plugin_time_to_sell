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
targetPaymentMethod = args["outcomeMethod"]
targetCurrency = args["currencyToSell"]
targetBuyCurrencyWallet = args["accountWallet"]
investMoney = args["outcome"]
targetAmountToBuy = args["trade"]


