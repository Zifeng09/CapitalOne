import nessie
class accounts():
    def __init__(self,type,nickname,rewards,balance,customer_id):

        self.type = type
        self.nickname=nickname
        self.rewards=rewards
        self.balance=balance
        self.customer_id=customer_id
    def createAccounts(self):
        payload = {
            'type':self.type,
            'nickname':self.nickname,
            'rewards':self.rewards,
            'balance':self.balance,

            }

        client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer');
        print(client.api_call('customers/{}/accounts'.format(self.customer_id),"POST",payload))

##TestCode
accounts = accounts('Credit Card','credit cards',500,5000,'58ea1e88ceb8abe24250d1d3')
accounts.createAccounts()