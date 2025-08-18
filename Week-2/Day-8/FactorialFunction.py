# Q : Function to return the factorial of a number (iterative & recursive).

def Factorial_Iterative(n):
    '''function to return factorial of a number (iterative)'''
    fact = 1
    for i in range(1,n+1):
        fact*=i
        
    return fact

def Factorial_Recursive(n):
    '''function to return factorial of a number (recursive)'''

    if n==0 or n==1:
        return 1
    
    return n*Factorial_Recursive(n-1)

number = int(input("Enter the number to calculate factorial :"))
print("Factorial of {0} : {1} (iterative)".format(number,Factorial_Iterative(number)))
print("Factorial of {0} : {1} (recursive)".format(number,Factorial_Recursive(number)))

