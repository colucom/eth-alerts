import factory
from faker import Factory as FakerFactory
import simplejson

faker = FakerFactory.create()


class Model(object):

    def __init__(self, abi, deletion_data, creation_data):
        self.abi = abi
        self.deletion_data = deletion_data
        self.creation_data = creation_data


class APIFactory(factory.Factory):

    class Meta:
        model = Model

    @factory.LazyAttribute
    def abi(self):
        data = simplejson.loads('[{"inputs": [{"type": "address", "name": ""}], "constant": true, "name": "isInstantiation",' \
                   '"payable": false, "outputs": [{"type": "bool", "name": ""}], "type": "function"},' \
                   '{"inputs": [{"type": "address[]", "name": "_owners"}, {"type": "uint256", "name": "_required"},' \
                   '{"type": "uint256", "name": "_dailyLimit"}], "constant": false, "name": "create", "payable": false,' \
                   '"outputs": [{"type": "address", "name": "wallet"}], "type": "function"},' \
                   '{"inputs": [{"type": "address", "name": ""}, {"type": "uint256", "name": ""}],' \
                   '"constant": true, "name": "instantiations", "payable": false, "outputs":' \
                   '[{"type": "address", "name": ""}], "type": "function"}, {"inputs": [{"type":' \
                   '"address", "name": "creator"}], "constant": true, "name": "getInstantiationCount",' \
                   '"payable": false, "outputs": [{"type": "uint256", "name": ""}], "type": "function"},' \
                   '{"inputs": [{"indexed": false, "type": "address", "name": "sender"}, {"indexed": false,' \
                   '"type": "address", "name": "instantiation"}], "type": "event", "name": "ContractInstantiation",' \
                   '"anonymous": false}]')

        return data

    @factory.LazyAttribute
    def creation_data(self):
        data = dict(abi=self.abi)

        data["contract"] = "0xd79426bcee5b46fde413ededeb38364b3e666097"
        data["email"] = faker.email()
        data["events"] = {
            "eventName": {
                "eventPropertyName": "eventPropertyValue"
            }
        }

        return data

    @factory.LazyAttribute
    def deletion_data(self):
        data = {
            "address": "0xd79426bcee5b46fde413ededeb38364b3e666097",
            "eventName": "eventName"
        }

        return data