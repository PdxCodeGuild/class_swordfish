'''Lab 9: ATM
'''
'''
Let's represent an ATM with a class containing two attributes:
-a balance and an interest rate.
-A newly created account will default to a balance of 0 and an interest rate of 0.1%.
-Implement the initializer, as well as the following functions:
    -check_balance() returns the account balance
    -deposit(amount) deposits the given amount in the account
    -check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
    -withdraw(amount) withdraws the amount from the account and returns it
    -calc_interest() returns the amount of interest calculated on the account
'''


class ATM:
    # create an instance of our class
    def __init__(self, balance=0, interest_rate=0.001):  # --> initializer
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []
        #self.transactions = ['user deposited $5', 'user withdrew $2']

    def __str__(self):
        return str(self.balance)

    def check_balance(self):
        # check_balance() returns the account balance
        return self.balance

# deposits the given amount in the account
    def deposit(self, amount):
        # print(self.transactions)
        self.balance += amount
        self.transactions.append(f'user deposited ${amount}')

# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative

    def check_withdrawal(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'user withdrew ${amount}')
        # withdraws the amount from the account and returns it
        return amount

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        # returns the amount of interest calculated on the account
        return interest

    def print_transactions(self):
        # self.transactions
        # print(self.transactions)
        for transaction in self.transactions:
            print(transaction)


atm = ATM()
# call the initilizer of the ATM class
print('Welcome to the ATM')


while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        # call the print_transactions method
        atm.print_transactions()

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
