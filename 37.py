# age = int(input("Enter your age: "))
# if 31 < age < 42:
#     print("Your age is between 31 and 41")
#
# years_of_experience = int(input("Enter your years of experience: "))
# if 2 < years_of_experience < 10:
#     print("Your years of experience is between 2 and 9")
#
#

def check_in_interval(what_to_ask, min_value, max_value, what_to_print):
    value = int(input(what_to_ask))

    if min_value < value < max_value:
        print(what_to_print)

def check_in_interval2(what_to_ask, min_value, max_value):
    value = int(input(what_to_ask))

    if min_value < value < max_value:
        return True
    return False

def square_value(number):
    return number * number



# Variable type defining

name: str = "Bob"    # Defining the variable type and assigning a value.

def say_hello(name: str) -> str:    # The arrow is defining the function return type.
    return f"Hello, {name}!"

 #########################

 # Function call
print(check_in_interval("Enter your age: ", 31, 42, "Your age is between 31 and 41"))

result = check_in_interval2("Enter your age: ", 31, 42)
if result:
    print("Your age is between 31 and 41")

print(square_value(5))