# Q : Write a function to check if a number is prime.

def checkPrime(num):
    ''' check whether number is prime or not.'''
    if num <=1:
        return False
    
    for i in range(2,num):
        if num%i==0:
            return False
    return True

number = int(input("Enter the number to check whether it's a prime:"))


print("{} is a Prime number.".format(number) if checkPrime(number) else "{} is not a Prime number.".format(number))
