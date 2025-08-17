# Mini Project:
# Q : Simple Calculator – Supports +, -, *, /; handles division by zero.

while True :
    print("Calculator".center(20,'-'))
    print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit")
    
    choice = int(input("Enter the choice (1,2,3,4) : "))
    if 0< choice <=4 :
        num1 = int(input("Enter the number 1 : "))
        num2 = int(input("Enter the number 2 : "))
    result = ''
    
    match(choice):
        case 1:
            result = f"Addition of {num1} and {num2} : {num1 + num2}"
        case 2:
            result = f"Subtraction of {num1} and {num2} : {num1 - num2}"
        case 3:
            result = f"Multiplication of {num1} and {num2} : {num1 * num2}"
        case 4:
            if num2!=0:
                result = f"Division of {num1} and {num2} : {num1 / num2}"
            else :
                result = f"Error: division by zero"
        case 5:
            print("exit...")
            break
        case _:
            print("Invalid Operation, try again (1,2,3,4 or 5)")

    if 0< choice <=4 :
        print("Result".center(20,'-'))
        print(result)
