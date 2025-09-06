# Q : Write a generator function for Fibonacci numbers.

#  Generator
#  A generator is a simpler way to create an iterator using a function with yield.
#  Each time the function is called, execution pauses at yield and resumes from there next time.
#  Generators are memory-efficient because they produce values one by one (lazy evaluation).

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a   # yield current number
        a, b = b, a + b   # update values

# Using the generator
fibo = fibonacci(10)

for i in fibo:
    print(i, end=" ")
