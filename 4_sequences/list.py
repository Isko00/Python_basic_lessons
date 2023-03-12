myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(myList)
# print(len(myList))

# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

print(myList[1])
print(myList[2:5])
print(myList[:4])
print(myList[2:])
print(myList[-4:-1])

if 4 in myList:
  print("Yes, 4 is in the list")

myList[1] = 999
print(myList)

myList[1:2] = [21, 22]
print(myList)