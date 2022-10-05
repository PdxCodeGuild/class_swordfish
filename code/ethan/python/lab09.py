#  ATM

import math

class ATM():
    def __init__(self):
        self.balance = 0    
        self.interest = .001
        self.transaction_histroy = []
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        statement = f'user deposited ${amount}'
        self.transaction_histroy.append(statement)
        self.balance = self.balance + amount
        return self.balance
    def check_withdrawal(self, amount):
        return self.balance >= amount
    def withdraw(self, amount):
        statement = f'user withdrew ${amount}'
        self.transaction_histroy.append(statement)
        self.balance = self.balance - amount
        return self.balance
    def calc_interest(self):
        amount = self.balance * self.interest
        return amount
    def print_transactions(self):
        return self.transaction_histroy




atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        transactions = atm.print_transactions()
        for i in transactions:
            print(i)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get transaction history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')