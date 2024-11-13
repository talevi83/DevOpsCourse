e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = []
print(len(e))

if len(e) > 8:
    print("enough items")

if e:
    print("e is not empty")

if not f:
    print("f is empty")

names = ["Tal", "Levi", "David", "Yosef"]
if "David" in names:
    print("David in in the building!!")

if type(names) is list:
    print("names is a list")

if isinstance(names, list):
    print("names is a list")

