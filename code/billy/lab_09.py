'''
program: lab_09
author: billy frick

date: 22 september 2022

function:   > This program will simulate an ATM for the user.
            > The user will be able to input a command or "help" for a list of commands.

'''

class ATM:

    def __init__(self):

        # default balance.
        self.balance = 0

        # default self interest.
        self.interest = 0.1

        # this will append each user transaction for later use.
        self.transactions = []

    # checks the balance of the users account.
    def check_balance(self):

        self.transactions.append(f'The user checked the balance of the account (${self.balance}).')

        return self.balance

    # deposits the users amount and adds it to the balance.
    def deposit(self, deposit_amount):

        self.deposit_amount = deposit_amount

        self.transactions.append(f'The user deposited ${deposit_amount}.')

        self.balance += self.deposit_amount

    # for line 96 'if statement'. Checks balance to ensure it is greater than the amount requested.
    def check_withdrawal(self, amount):

        return self.balance > amount

    # withdraws the users amount given, and subtracts it from the balance.
    def withdraw(self, amount):

        self.balance -= amount

        self.transactions.append(f'The user withdrew ${amount}.')

        return amount

    # calculates interest based off of the balance. Unsure which form of interest formula should be used.
    def calculate_interest(self):

        amount = round(self.balance * self.interest)

        self.transactions.append(f'The user has accrued ${amount} of interest.')

        return amount

    # returns the list 'transactions' which has appended each user transaction from the other functions.
    def print_transactions(self):

        return self.transactions




# main code.
# this program will run until the user enters command 'exit'

# create an instance of our class
atm = ATM() 

print('\nWelcome to the ATM')

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

        amount = atm.calculate_interest() # call the calc_interest() method

        atm.deposit(amount)

        print(f'Accumulated ${amount} in interest')

    # allows user to input 'transactions' and have a list printed off.
    elif command == 'transactions':

        transactions = atm.print_transactions()

        print(f"\n|----------your transaction history--------------|\n")

        # for loop will print out each transaction in the list; on a new line.
        for x in range(len(transactions)):
            print(' >>',transactions[x])

        print("\n|-----------end of your transactions--------------|\n")

    elif command == 'help':

        print('Available commands:')

        print('balance  - get the current balance')

        print('deposit  - deposit money')

        print('withdraw - withdraw money')

        print('interest - accumulate interest')

        # added print function for transactions list.
        print('transactions - print a list of your previous transactions')

        print('exit     - exit the program')

    elif command == 'exit':

        break

    else:

        print('Command not recognized')