import requests

import pprint

# response = requests.get('https://developer.trimet.org/ws/v2/vehicles?appID=D065A3A5DAE4622752786CEB9&routes=20')
response = requests.get('https://developer.trimet.org/ws/v2/vehicles', params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': 20})

print(response.url)
# print(response.text)
print(response.status_code)
print(response.encoding)
print(response.headers)

results = response.json()

pprint.pprint(results)

for bus in results['resultSet']['vehicle']:
    print(f'{bus["signMessage"]} -- {bus["vehicleID"]}')