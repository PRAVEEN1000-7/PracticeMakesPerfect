# Q : Write a program to swap two variables (with and without a temp variable).


num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

# with a temp variable :
print("before swapping :")
print("first number: {0} and second number: {1}".format(num1,num2))
temp = num1
num1 = num2
num2 = temp
print("after swapping :")
print("first number: {0} and second number: {1}\n".format(num1,num2))

# without a temp variable :
print("without a temp variable")
print("by using (,):")

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

print("after swapping :")
print("first number: {0} and second number: {1}".format(num1,num2))
num1,num2 = num2,num1
print("after swapping :")
print("first number: {0} and second number: {1}\n".format(num1,num2))

# without temp and using bitwise operator.
print("without a temp variable")
print("by using (Bitwise-operator):")

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

print("after swapping :")
print("first number: {0} and second number: {1}".format(num1,num2))

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print("after swapping :")
print("first number: {0} and second number: {1}".format(num1,num2))
