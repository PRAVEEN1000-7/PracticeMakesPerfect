# Q : Handle division by zero with try/except.

try :
    print("Division Operation".center(30,'='))
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    result=num1/num2
    print("the result : {}".format(result))
except ZeroDivisionError:
    print("ERROR : division by zero is not allowed!")
except ValueError:
    print("ERROR : please enter a valid integers!")
