import requests

param = {'node1': 'node_0-0', 'node2': 'node_0-1', 'bw': 1, 'delay': '200ms', 'jitter': '50ms', 'loss':1}

data_list = []
data_list.append(param)


requests.post(r'http://127.0.0.1:8000/modify/', json=data_list)