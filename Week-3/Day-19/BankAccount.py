
class BankAccount :
    
    # intializing account
    def __init__(self,acc_id, acc_holder, balance) :
        self.acc_id = acc_id
        self.acc_holder = acc_holder
        self.balance = balance
        
    # deposit amount
    def Deposit(self, amount) :
        
        if amount > 0 :
            self.balance += amount
            print(f"Deposited amount: {amount}")
            print(f"new balance : {self.balance}")
        else:
            print("Invalid deposit amount")
    
    # withdraw amount
    def withDraw(self,amount) :
        
        if amount <=0:
            print("Invalid withdrawal amount")
        
        elif amount > self.balance :
            print("Insufficient balance")
        
        else :
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"new balance : {self.balance}")
            
    
    # Balance checking
    def checkBalance(self):
        print(f"Current Balance: {self.balance}")
        
    def __str__(self):
        return f"BankAccount({self.acc_holder}, Balance: {self.balance})"
    
    def __repr__(self):
        return f"BankAccount(account_number={self.acc_id}, account_holder='{self.acc_holder}', balance={self.balance})"

    
# sample usage :

user = BankAccount(12344,"John wick",10000)

user.checkBalance()
user.Deposit(5000)

user.checkBalance()
user.withDraw(2500)

user.checkBalance()

print(user)
print(str(user))
print(repr(user))