import datetime
# import mydep
from mydep import test


def wait_for_print():
    from time import sleep
    sleep(3)
    print("Hello World!")


print(datetime.datetime.now())
# mydep.test()

test()


