def addition(a, b):
    print(a + b)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print all fibonacci numbers up to n
def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i))

# addition(1, 2)
# addition(2, 3)

print_fibonacci(10)