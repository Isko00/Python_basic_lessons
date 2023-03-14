thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    # two items with same key can not be added
    # "year": 2020,
    "isRepaired": True,
    "hasOwner": False,
    "colors": ["red", "white", "blue"]
}

print(thisdict)

print(thisdict["brand"])

print(len(thisdict))

print("    keys: ", thisdict.keys())

for x in thisdict:
    print(x, end=' ')
print()

print("    values: ", thisdict.values())

for x in thisdict:
    print(thisdict[x], end=' ')
print()

for x, y in thisdict.items():
    print(x, y)

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in this dictionary")

thisdict["year"] = 2018
print(thisdict)

thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["year"]
print(thisdict)

# thisdict.clear()
# print(thisdict)

myDict2 = thisdict.copy()
print(myDict2)

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Shamil",
    "year": 2007
}
child3 = {
    "name": "Dinara",
    "year": 2011
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myFamily["child2"]["name"])

