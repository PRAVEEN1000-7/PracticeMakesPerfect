import itertools
from itertools import accumulate, chain, compress, pairwise, product, permutations, combinations

r = range(1,10)
i = iter(r)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for j in i:
    print(j)
    
'''
Infinite Iterators
These run forever (until you stop them).
count(start=0, step=1)
Keeps counting numbers.
'''
for i in itertools.count(10,2):
    if i==20:
        break
    print(i)
    
'''
cycle(iterable)
Repeats elements of iterable forever.'''
count=0
for i in itertools.cycle("ABC"):
    print(i,end=" ")
    count+=1
    if count ==10:
        break
print()
'''
repeat(object, times=None)
Repeats an object multiple times.'''
for i in itertools.repeat("hello",3):
    print(i)

'''terminating iterator'''

'''Running totals or custom accumulations.'''
running_sum = accumulate(range(1,11))
print(list(running_sum))

'''Combines multiple iterables into one.'''
chaining = chain("ABC","DEF")
print(list(chaining))

'''chain.from_iterable() is a variant of itertools.chain() that flattens a single iterable of iterables.'''
iterchain = [[1,2,3],[4,5,6],[7,8,9]]
print(list(chain.from_iterable(iterchain)))

'''compress(data, selectors)
Filters elements from data returning only those for which the corresponding element in selectors is True.'''
data = [[1,2,3],['a','b','c'],[0,1,0]]
print(list(compress(data,[True,False,True])))

'''pairwise(iterable)
Returns an iterator of pairs from the iterable.'''
print(list(pairwise([1,2,3,4,5,5,6,7,8,9,10])))

'''product(*iterable, repeat=1)
Returns the Cartesian product of the input iterable.'''
print(list(product([1,2,3],['a','b','c'])))

'''permutations(iterable, r=None)
Returns all possible permutations of the input iterable.'''
print(list(permutations([1,2,3],2)))

'''combinations(iterable, r)
Returns all possible combinations of length r from the iterable.'''
print(list(combinations([1,2,3],2)))