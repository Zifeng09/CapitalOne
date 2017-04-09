import nessie
class customers():

    def __init__(self,streetNo,streetName,city,state,zip):
        self.streetNo = streetNo
        self.streetName = streetName
        self.city = city
        self.state = state
        self.zip=zip
        self.payload= {
            "first_name":"LL",
            "last_name":'lll',
            "address":
            {"street_number":self.streetNo,
            "street_name":self.streetName,
            "city":self.city,
            "state":self.state,
            "zip":self.zip
            }
        }
        client = nessie.NessieClient('682bc88f420a505fb5d69090d0b8c924','customer');
        self.customer_data = client.api_call("customers", "POST", self.payload)['content']['objectCreated']
        self._id = self.customer_data['_id']

    def _id(self):
        return self._id

    def data(self):
        return self.customer_data