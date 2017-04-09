import nessie
import datetime
def transfer(transaction_date,medium,payee_id,amount):
    payload = {
        "transaction_date":transaction_date,
        "medium":medium,
        "payee_id":payee_id,
        "amount":amount
    }
    client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer')
    print(client.api_call("accounts/{}/transfers".format(payee_id),"POST",payload))

def withdraw(transaction_date,medium,payee_id,amount):
    payload = {
        "transaction_date": transaction_date,
        "medium": medium,
        "payee_id": payee_id,
        "amount": amount
    }
    client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer')
    print(client.api_call("accounts/{}/withdrawals".format(payee_id), "POST", payload))

def deposit(transaction_date,medium,payee_id,amount):
    payload = {
        "transaction_date": transaction_date,
        "medium": medium,
        "amount": amount
    }
    client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer')
    print(client.api_call("accounts/{}/deposits".format(payee_id), "POST", payload))
  #  print("Current balance is :" +client.api_call("accounts/{}".format(payer_id))

#transfer
transfer(datetime.datetime.now().strftime("%Y-%m-%d"),"balance","58e9ba55a73e4942cdafd421",200.25)
#deposit
deposit(datetime.datetime.now().strftime("%Y-%m-%d"),"balance","58e9ba55a73e4942cdafd421",200.25)
#withdraw
withdraw(datetime.datetime.now().strftime("%Y-%m-%d"),"balance","58e9ba55a73e4942cdafd421",200.25)