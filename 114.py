import requests

response = requests.get('https://www.wikipedia.org/')
if response.status_code == 200:
    print('Wikipedia page found')
elif response.status_code == 404:
    print('Wikipedia page not found')


