class Wallet:
   '''
   Docstring for Wallet
    This class represents a simple wallet that can hold a balance and allows for deposits and withdrawals.
    Attributes:
    - __balance: a private attribute that holds the current balance of the wallet
    Methods:
    - __init__: initializes the wallet with a balance of 0
    - __validate: a private method that checks if the amount is valid (positive) and raises a ValueError if it is not
    - deposit: a method that allows the user to deposit money into the wallet, it uses the __validate method to check if the amount is valid before adding it to the balance
    - withdraw: a method that allows the user to withdraw money from the wallet, it uses the __validate method to check if the amount is valid before subtracting it from the balance, and also checks if there are sufficient funds before allowing the withdrawal
    - get_balance: a method that returns the current balance of the wallet
    
   '''
   def __init__(self):
       self.__balance = 0 #this is a private attribute

   def __validate(self, amount):
       '''
       Docstring for __validate
       
       :param self: class instance
       :param amount: the amount to validate
       :raises ValueError: if amount is negative
       :return: None
       this method checks if the amount is valid (positive) and raises a ValueError if it is not.
       also is a private method, meaning it can only be accessed within the class and not from outside.
       '''
       if amount < 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = Wallet()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds