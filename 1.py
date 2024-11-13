a = 4
b = "tal"
c = True
d = ["tal", "levi", 40, True]
e = {"firstName": "Tal", "lastName": "Levi", "Age": "40", "Relationship status": "Known In Public"}
f = dict(firstName="tal", lastName="Levi", age=40) # Dictionary - this is like Map in Java.
list_of_people = [e, f]
print(e["firstName"])
print(e["lastName"])
print(a)
print("name is: " + b)
print(c)

r = 4 + 4
s = "Tal" + "Levi"
t = "Tal " * 4
u = "Tal " + str(4) # Casting like in Java / C
print(t)
print(u)

fName = "Tal"
lName = "Levi"
first = fName + " " + lName
second = "{} {}".format(fName, lName) # Like String.format in Java to concatenate Strings
third = f"{fName} {lName}"

print(first)
print(second)
print(third)
