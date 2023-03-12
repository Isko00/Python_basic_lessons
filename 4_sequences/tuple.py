myTuple = (1, 2, 3)
print(myTuple)

# tuple1 = ("abc", 34, True, 40, "male", True, 40, "male")
# print(tuple1)

print(len(myTuple))

# myTuple = ("apple",)
# print(type(myTuple))
# #NOT a tuple
# myTuple = ("apple")
# print(type(myTuple)) 

print(myTuple[1])
print(myTuple[-1])
print(myTuple[2:5])
print(myTuple[:4])
print(myTuple[2:])
print(myTuple[-4:-1])
if 4 in myTuple:
    print("Yes, 4 is in the tuple")

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 

fruits = ("apple", "banana", "cherry")
myTuple = fruits * 2

print(myTuple) 