# Before
import requests

my_file = open('names.txt', 'r')
names = my_file.read().splitlines()
for name in names:
    print(name)
my_file.close()


# After - if something went wrong, the scope will be closed and the script will stop execution.
with open('names.txt', 'r') as my_file:
    names = my_file.read().splitlines()
    for name in names:
        print(name)

with requests.get('https://www.wikipedia.org/') as response:
    response.raise_for_status()