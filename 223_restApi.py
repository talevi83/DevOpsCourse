import requests

base_url = 'http://127.0.0.1:5000/'
response = requests.get(base_url + '/names')
results = response.json()

expected = "Tal"
actual = results[0]["name"]
assert actual == expected, "The expected is not match to the actual"

print(results)
# print(response.text)
# print(response.status_code)