# Q : Given three numbers, find the largest (without using max()).

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the three number :"))

if (num1>num2) and (num1>num3):
    print(f"{num1} is greater.")
elif (num2>num3):
    print(f"{num2} is greater.")
else:
    print(f"{num3} is greater.")