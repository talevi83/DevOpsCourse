current_name = input("What is your name? ")

while current_name != "quit":
    print(f"Hello {current_name}!")
    current_name = input("What is your name? ")

else:
    print("Goodbye!")