# Q : Raise a ValueError if input is negative.

try :
    age = int(input("Enter the age :"))
    if age < 0:
        raise ValueError("ERROR : age can't be negative!")
    print(f"You're age is {age}")
except ValueError as e:
    print("ERROR : ",e)
    