import requests
url = 'https://data.gov.gr/api/v1/query/minenv_inspectors'
headers = {'Authorization':'Token 87a465af94af31194a24dcadf7e12b3c9e22b366'}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
print(response.encoding)
print(response.headers)