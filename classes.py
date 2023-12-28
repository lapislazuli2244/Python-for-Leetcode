class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
        
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 + self.getLength()

obj = MyClass([1,2,3])
print(obj.getLength())