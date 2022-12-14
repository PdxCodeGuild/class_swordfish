class ATM:
    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transaction = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.transaction.append(f'{user_name} Deposited ${amount}')
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        return self.balance > amount

    def withdraw(self,amount):
        self.transaction.append(f'{user_name} Withdrew ${amount}')
        self.balance -= amount
        return self.balance

    def calc_interest(self):
        return round(self.balance * self.interest + self.interest,2)

    def print_transactions(self):
        for transaction in self.transaction:
            print(transaction)

#---------------------------------------------------------------------------


atm = ATM() # create an instance of our class
print('Welcome to the ATM')
user_name = input("Please enter your name: ")

while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit?: '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')

    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw?: '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions    - see your previous transactions')
    elif command == 'transactions':
        atm.print_transactions()
    elif command == 'exit':
        break
    else:
        print('Command not recognized')