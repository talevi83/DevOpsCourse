current_name = input('What is your name? ')

my_file = open('names.txt', 'a')    # Open with 'a' means append
my_file.write(current_name + '\n')
my_file.close()

my_file = open('names.txt', 'r')    # Open with 'r' means read
for name in my_file.readlines():
    print(f'Hello {name}')

my_file.close()