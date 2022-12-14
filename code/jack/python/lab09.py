# Lab 9: ATM machine

class ATM():
    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount, interest = False):
        if interest == False:
            self.transactions.append(f'deposit: +${amount}')
        self.balance += amount

    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True

    def withdraw(self, amount):
        self.transactions.append(f'withdraw: -${amount}')
        self.balance -= amount
        
    def calc_interest(self):
        amount = self.balance * self.interest
        self.transactions.append(f'interest: +${amount}')
        return amount
    
    def print_transactions(self):
        return self.transactions



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
        atm.deposit(amount, True) # passes True into deposit 'interest' attribute for use in transaction history
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
        print('transactions - print transactions history')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')