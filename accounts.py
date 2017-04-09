import nessie
class accounts():
    def __init__(self,type,nickname,rewards,balance,customer_id):

        self.type = type
        self.nickname=nickname
        self.rewards=rewards
        self.balance=balance
        self.customer_id=customer_id
        self.payload = {
            'type':self.type,
            'nickname':self.nickname,
            'rewards':self.rewards,
            'balance':self.balance,

        }

        # create an account
        client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924', 'customer');
        self.account_data = client.api_call('customers/{}/accounts'.format(customer_id),"POST", self.payload)['content']['objectCreated']
        self._id = self.account_data['_id']

    def _id(self):
        return self._id

    def data(self):
        return self.account_data