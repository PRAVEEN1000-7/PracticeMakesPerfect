# Q : Given a number, check if it’s odd or even.

num = int(input("Enter the number to check whether it's odd or even? :"))

# by using bitwise operator (&)
if ((num & 1)==0):
    print(f"the given number {num} is even.")
else:
    print(f"the given number {num} is odd.")

#by using modulo operator
num = int(input("Enter the number to check whether it's odd or even? :"))
if (num % 2 == 0):
    print(f"the given number {num} is even.")
else:
    print(f"the given number {num} is odd.")
    