class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

   
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        print(f"The amount left in your account is ${self.account_balance}")
               
           
          