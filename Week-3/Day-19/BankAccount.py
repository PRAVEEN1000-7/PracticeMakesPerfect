
class BankAccount :
    
    # intializing account
    def __init__(self,acc_id, acc_holder, balance) :
        self.acc_id = acc_id
        self.acc_holder = acc_holder
        self.__balance = balance
        
    # deposit amount
    def Deposit(self, amount) :
        
        if amount > 0 :
            self.__balance += amount
            print(f"Deposited amount: {amount}")
            print(f"new balance : {self.__balance}")
        else:
            print("Invalid deposit amount")
    
    # withdraw amount
    def withDraw(self,amount) :
        
        if amount <=0:
            print("Invalid withdrawal amount")
        
        elif amount > self.__balance :
            print("Insufficient balance")
        
        else :
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"new balance : {self.__balance}")
            
    
    # Balance checking
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter    
    def balance(self,amount):
        if amount > 0 :
            self.__balance = amount
        else:
            print("balance can't be negative !")
    
    
    def __str__(self):
        return f"BankAccount({self.acc_holder}, Balance: {self.__balance})"
    
    def __repr__(self):
        return f"BankAccount(account_number={self.acc_id}, account_holder='{self.acc_holder}', balance={self.__balance})"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.__balance + other.__balance
        return NotImplemented
    
    def __len__(self):
        return len(self.acc_holder)
    
# sample usage :

acc1 = BankAccount(101, "John Wick", 10000)
acc2 = BankAccount(102, "John Wick", 5000)

acc1.Deposit(2000)
acc1.withDraw(3000)

print(acc1.balance)
acc1.balance = 7000
print(acc1.balance)


print(acc1)
print(repr(acc2))

print("Total Balance : {}".format(acc1 + acc2))
print("Name Length : {}".format(len(acc2)))