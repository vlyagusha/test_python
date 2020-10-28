import http.client

HOST = 'localhost'
PORT = 8080

connection = http.client.HTTPConnection(HOST, port=PORT)
connection.request('GET', '/')
response = connection.getresponse()
body = response.read().decode()
print('Response is:', body)
