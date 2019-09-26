# Coinbase Plugin Time To Sell 
This is a Nagios Plugin to monitor sell rates of specific Crypto Currencies on Coinbase.

## Purpose
The goal of this script is to monitor current sell rates for various Crypto Currencies on Coinbase, including the fees.
### When should I use this plugin?
If you have in your head something like: "I want to sell one of my Bitcoins for 10.000$." - This is the plugin you were looking for.
### Why should I use this plugin?
Due to the fact that Coinbase has really high fees it's interesting to monitor the sell prices including the fees without checking the app or web interface all the time.
Connecting this script with Icinga or Nagios makes it even easier to automatically start processes if your desired price is currently live.

## Functionality
This script works using the official Coinbase API (key and secret).  
The plugin has been written in Python which gives it the additional feature to use the official Coinbase Python Library.  
The plugin also returns the current outcome for the defined amount and target combination as performance data.

## Requirements
* argparse
* coinbase
### Requirements installation
`pip install argparse`  
`pip install coinbase` 

## Usage
Just call the script using the following parameters and input values:  
`./check_cbTimeToSell.py -k <API Key> -s <API Secret> -c <Which Crypto do you want to sell> -a <Crypto Wallet> -t <Amount of Crypto you want to sell> -m <Your desired outcome method> -o <How much of your outcome Method do you want to receive>`

Example:  
`./check_cbTimeToSell.py -k 'xxxxxxxxxxxxxxxx' -s 'xxxxxxxxxxxxxxxxxxxxxx' -c 'BTC' -a 'BTC Wallet' -t '1' -m 'USD Wallet' -o '10000.00'`

## Exit Codes
|Code|Nagios State|Description|Output|
|---|---|---|---|
|0|OK - Green|The desired outcome for the specified currency is not reached|Your desired target outcome is not reached yet. Keep waiting! \| outcome=\<value\> |
|2|Critical - Red|The desired outcome for the specified currency is reached.|Your desired target outcome is reached! \| outcome=\<value\> |

