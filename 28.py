# Seven-BOOM!

for i in range(1, 101):
    if i % 7 == 0:
        print("BOOM!")
    if "7" in str(i):
        print("BOOM!!!!!")
    else:
        print(i)


# list comprehension
result = [i for i in range(1, 101) if i % 7 != 0 or "7" not in str(i)]
print(result)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
resultNames = [name.upper() for name in names if "a" in name]   # only names with 'a' in them will be uppercased.
              # what to do  | for each loop   | condition

print(resultNames)
