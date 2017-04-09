from customers import customers
from accounts import accounts
from activities import *
import datetime
import urllib
import json

# Our Exchange's own account and it's amount is preset
exchange_cust_id = '58e9ba55a73e4942cdafd420' # Bethel Predovic
exchange_acct_id = '58e9ba55a73e4942cdafd421' # Audie's credit card

# the example customer to use
example_cust_id = '58e9ba54a73e4942cdafd41e' # Marianna Eichmann
example_acct_id = '58e9d75fceb8abe24250c14e' # Savings account

# obtain the current Bitcoin price
def bitcoinPriceGrab():
    with urllib.request.urlopen("https://blockchain.info/ticker") as url:
        data = json.loads(url.read().decode())

    return data['USD']['15m']

# convert usd value to bitcoin
def usdtobitcoin(usd_amt):
    return float(usd_amt)/bitcoinPriceGrab()

# convert bitcoin value to usd
def bitcointousd(btc_amt):
    return float(btc_amt)*bitcoinPriceGrab()

# dispense a certain amount of BTC for USD
def disp_USD2BTC(account_id, usd_amt):
    btc_amt = usdtobitcoin(usd_amt)

    # transfer from customer to exchange
    transfer(datetime.datetime.now().strftime("%Y-%m-%d"), "balance", account_id, exchange_acct_id, usd_amt)

    # return the amount of BTC sent
    return btc_amt

# dispense a certain amount of USD for BTC
def disp_BTC2USD(account_id, btc_amt):
    usd_amt = bitcointousd(btc_amt)

    # transfer from exchange to customer
    transfer(datetime.datetime.now().strftime("%Y-%m-%d"), "balance", exchange_acct_id, account_id, usd_amt)

    # return the amount of USD sent
    return usd_amt

'''
# create customer (not used yet)
customer = customers('123', 'Example St.', 'Example City', 'EX', '00000')

# create account (not used yet)
account = accounts('Credit Card','credit cards',500,5000,customer._id)


#transfer (superseded by dispBTC2USD)
transfer(datetime.datetime.now().strftime("%Y-%m-%d"),"balance",example_acct_id, account._id,200.25)

#deposit
deposit(datetime.datetime.now().strftime("%Y-%m-%d"),"balance",account._id,200.25)
#withdraw
withdraw(datetime.datetime.now().strftime("%Y-%m-%d"),"balance",account._id,200.25)

'''