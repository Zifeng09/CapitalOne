import nessie
def transfer(transaction_date,medium,payer_id,payee_id,amount):
    payload = {
        "transaction_date":transaction_date,
        "medium":medium,
        "payee_id":payee_id,
        "amount":amount
    }
    client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer')
    print(client.api_call("accounts/{}/transfers".format(payer_id),"POST",payload))

def show_transfers(account_id):
    client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer')
    return client.api_call("accounts/{}/transfers".format(account_id),"GET")

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