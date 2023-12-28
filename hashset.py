print()
mySet = set()

print("Sets")
mySet.add(1)
mySet.add(2)
mySet.add(3)

mySet.remove(1)
print(mySet)
print(10 in mySet)
print("Set Comprehension: ",{i for i in range(1, 5, 1)})