
def outer(a, b):
    c = 22
    def inner():
        return a + b + c
    return inner()

print()
print('Value is: ',outer(1, 1))