import requests

response = requests.request('GET', 'http://httpbin.org/get')
print(response.text)
