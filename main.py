import http.client
import json
from pprint import pprint

HOST = 'httpbin.org'

connection = http.client.HTTPConnection(host=HOST, port=80)
# connection.request('GET', '/get')
# response = connection.getresponse()
# body = response.read().decode()
# res = json.loads(body)
# pprint(res)

headers = {
    'Content-Type': 'application/json'
}
my_data = {
    'key': 'value',
    'spam': 'eggs',
    'what?': 42
}
request_body = json.dumps(my_data)
connection.request('POST', '/post', request_body, headers=headers)
data = json.loads(connection.getresponse().read().decode())
pprint(data)
print('Eq?', data['json'] == my_data)
