import requests
from time import sleep

try:
    response = requests.get('https://.myhuboflevifamily.com')
except BaseException as e:      # Like to use catch(Exception e) in Java
    print(f"getting HTTP response error: {e.args}")

time_to_sleep = int(input('time_to_sleep: '))
sleep(time_to_sleep)


a = int(input('First: '))
b = int(input('Second: '))
res = (a / b)
print('Result:', res)