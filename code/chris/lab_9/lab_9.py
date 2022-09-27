import math

#Version1

# class ATM:     # this will share all below functions. everything below will share same variables.
#     #how to tell if new account?
#     def __init__(self):  #call the initializer and this runs the CLASS #new account default to $0 and 0.1% interest
#         self.balance = 0 #member variables
#         self.interest_rate = .001

#     def check_balance(self):
#         balance = self.balance
#         return balance

#     def deposit(self, amount):
#         deposit = amount
#         self.balance += deposit
#         return deposit

    # def check_withdrawal(self, amount):
    #     if self.balance > amount:
    #         return True

    # def withdraw(self, amount):
    #     withdraw = amount
    #     self.balance -= withdraw
    #     self.transactions_list.append(f'user withdrew {withdraw}')
    #     return withdraw
    
#     def calc_interest(self):
#         return (self.interest_rate * self.balance)

# atm = ATM() # create an instance of our class
# print('Welcome to the ATM')
# while True:
#     command = input('Enter a command: ')
#     if command == 'balance':
#         balance = atm.check_balance() # call the check_balance() method
#         print(f'Your balance is ${balance}')
#     elif command == 'deposit':
#         amount = float(input('How much would you like to deposit? '))
#         atm.deposit(amount) # call the deposit(amount) method
#         print(f'Deposited ${amount}')
#     elif command == 'withdraw':
#         amount = float(input('How much would you like '))
#         if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
#             atm.withdraw(amount) # call the withdraw(amount) method
#             print(f'Withdrew ${amount}')
#         else:
#             print('Insufficient funds')
#     elif command == 'interest':
#         amount = atm.calc_interest() # call the calc_interest() method
#         atm.deposit(amount)
#         print(f'Accumulated ${amount} in interest')
#     elif command == 'help':
#         print('Available commands:')
#         print('balance  - get the current balance')
#         print('deposit  - deposit money')
#         print('withdraw - withdraw money')
#         print('interest - accumulate interest')
#         print('exit     - exit the program')
#     elif command == 'exit':
#         break
#     else:
#         print('Command not recognized')

#Version2

class ATM:     # this will share all below functions. everything below will share same variables.
    #how to tell if new account?
    def __init__(self):  #call the initializer and this runs the CLASS #new account default to $0 and 0.1% interest
        self.balance = 0 #member variables
        self.interest_rate = .001
        self.transactions_list = []

    def print_transactions(self):
        print(self.transactions_list)
    
    def check_balance(self):
        balance = self.balance
        return balance

    def deposit(self, amount):
        deposit = amount
        self.balance += deposit
        self.transactions_list.append(f'user deposited {deposit}')
       
    def check_withdrawal(self, amount):
        if self.balance > amount:
            return True

    def withdraw(self, amount):
        withdraw = amount
        self.balance -= withdraw
        self.transactions_list.append(f'user withdrew {withdraw}')
        return withdraw
    
    def calc_interest(self):
        return (self.interest_rate * self.balance)

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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get a list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')