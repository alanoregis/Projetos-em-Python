from client_code import client_code
from data_dict import DataDict
from data_list import DataList
from adapter import AdapterListToDict

data = DataDict()

data_list = DataList()
print(data_list.get_clients_list())

adapter = AdapterListToDict()
print(adapter.get_clients())