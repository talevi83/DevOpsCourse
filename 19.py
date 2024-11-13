
a = "tal"

print(list(range(5)))           # print 0 to 4.
print(list(range(1, 50, 10)))   # print 1 to 50 in steps of 10.
print(list(range(50, 10, -3)))  # print 50 to 10 in steps of -3.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for i in range(5):
    print(a + " ", end="")  # end="" to prevent newline, values in end will print at the end of the same line.

for name in names:
    print(f"hello {name}!")

print("\n*****************************\n")

for i in range(len(names)):
    print(f"hello {names[i]}!")

