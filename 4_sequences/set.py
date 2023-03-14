mySet = {"apple", "banana", "cherry", 1, True}
print(mySet)

for x in mySet:
    print(x)

print("cherry" in mySet)

mySet.add("orange")

numbers = {2, 4, 3}

mySet.update(numbers)

print(mySet)

myList = ["kiwi", "orange"]

mySet.update(myList)

print(mySet)

# Can cause error if item does not exist
mySet.remove("banana")

print(mySet)

# Can not cause error if item does not exist
mySet.discard("banana")

print(mySet)

while (len(mySet)) > 0:
    print(type(mySet.pop()))

mySet.clear()

print("qwe", mySet)

del mySet

#print(mySet)