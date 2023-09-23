#python program to create Bankaccount class
#with both a deposit() and a withdraw() function 
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit and Withdrawal Machine")

    def deposit(self):
        amount=float(input("Enter amount to be Deposited:"))
        self.balance += amount 
        print("\n Amount Deposited:",amount)

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount 
            print("\n you Withdrew:",amount)
        else:
            print("\n insufficient balance  ")
          
    def display(self):
        print("\n Net Available Balance=",self.balance)
          
# Driver code 

# creating an object of class 
s = Bank_Account()

# Calling function with that class object 
s.deposit()
s.withdraw()
s.display() 

