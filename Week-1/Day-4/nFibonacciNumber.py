# Q : Print the first n Fibonacci numbers.

n = int(input("Enter the range : "))

if n>0:
    a,b = 0,1
    print(f"{a} {b}" if n!=1 else a,end=' ')
    for i in range(n-2):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
else:
    print("the range must be greater than 0.")