# Assignment
import math

print("Greatest integer: ", float("inf"))
print("Smallest Integer: ", float("-inf"))

print(math.pow(2,200) < float("inf"))

print("\n")
print("Floor: ", math.floor(3/2));
print("Ceil: ",math.ceil(3/2))
print("Square root: ", math.sqrt(16))
print("Power of: ", math.pow(3,3))

print("\n")

print("Modulo Operator")
print(10 % 3, -10 % 3)

print("\nModulo operator using fmod:")
print(math.fmod(10, 3), math.fmod(-10, 3))

print("\n")
i  = 0
while i<=4:
    print(i)
    i += 1
    
print("\n")

print(  "for loop: (start, end-(not inclusive), increment) ")

for i in range(1,6,2):
    print(i)
    
    
print("\nfor loop: Reverse")
for i in range(10, 4, -1):
    print(i)
    

print("\nDivision")
print(-3/2)
print(-3//2, int(-3/2))