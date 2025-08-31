
class MathWorks:
    
    @staticmethod
    def factorial(n):
        fact = 1
        for i in range(1,n+1):
            fact*=i
            
        return fact
    
    @staticmethod
    def checkPrime(num):
        if num <=1:
            return False
        
        for i in range(2,num):
            if num%i==0:
                return False
        return True
    
    @staticmethod
    def square(n):
        return n**2
    
    @staticmethod
    def cube(n):
        return n**3