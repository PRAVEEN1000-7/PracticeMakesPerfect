# Q : Reverse a number using a loop.

number = int(input("Enter the number :"))

while number>0:
    last = number % 10
    print(last,end='')
    number //=10
