# Q : Build a custom iterator (EvenNumbers up to N).

# Iterator
# An iterator is an object that returns elements one at a time using the __next__() method.
# It follows the iterator protocol:
# __iter__() → returns the iterator object itself
# __next__() → returns the next value, or raises StopIteration when there are no more items.

# iterator example:
nums = [1, 2, 3]
it = iter(nums)   # get iterator
print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3

# custom iterator 
class EvenUptoN:
    
    def __init__(self, n):
        self.num = 0
        self.n = n
    
    def __iter__(self):
        return self  # an iterator returns itself
    
    def __next__(self):
        self.num += 2
        if self.num <= self.n:
            return self.num
        else:
            raise StopIteration   # must raise this to stop iteration

# Taking input
N = int(input("Enter the range for even number to print: "))

evenIter = EvenUptoN(N)

for num in evenIter:   
    print(num)
