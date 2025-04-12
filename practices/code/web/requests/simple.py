import requests

response = requests.get('https://www.google.com')

print(response.status_code, response.reason, end='\n\n')
print(response.headers, end='\n\n')
print(response.text)