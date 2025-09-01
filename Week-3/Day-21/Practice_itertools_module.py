import itertools

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