arr = [1,2,3]

print("\n")
print("Initial: ",arr)

arr.append(63)
print("After append: ", arr)

arr.pop()
print("After pop: ", arr)

arr.pop(2)
print("After pop with index: ", arr)

arr.insert(1,"Inserted string")
print("After insert: ", arr)

print("")

initial_arr = [1] * 4
print(initial_arr)

print("")

print("Looping with index")
random = [1,2,3,4,5]
for i in range(len(random)):
    print(random[i])
    
print("")

print("Looping without index")
for i in random:
    print(i)
    
print("")

print("Looping with index and value using enumerate")
for i,v in enumerate(random):
    print("index: ",i, " value: ",v)
    
# nums1 = [1,2,3]
# nums2 = [4,5,6]
# print(type (zip(nums1, nums2)))
# for i, j in zip(nums1, nums2):
#     print(i,j)
print("")

nums = [5, 7,4,2,1]
nums.sort()
print(nums)

print("")

str_arr = ['Joe', 'Bane', "Jane", 'Jolly', "Brigid"]
str_arr.sort(key = lambda x: len(x))
print(str_arr)

print("")

print([i for i in range(4) ])
print([i * 2 for i in range(4)])

print()

print("List comprehension for 2D lists")
nums = [ [1] * 4 for i in range(4) ]
print(nums)

print()

print("strings")
print(12 + int(123))

print(ord('A'))

print()

arr = ["aa", "bhf", 'jdh']
res = " ".join(arr)
print(res)