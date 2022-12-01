#ATM Lab Both Versions#

class ATM():
    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []

    def check_balance(self):
        self.transactions.append(f"Account Balance: ${self.balance}")
        return self.balance

    def deposit(self, amount):
            self.transactions.append(f"Amount Deposited: ${amount}")
            self.balance += amount
            return self.balance
       

    def check_withdrawal(self, amount):
        self.transactions.append(f"Withdrawal: ${amount}")
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance -= amount
        return amount
       
        
    def calc_interest(self):
       interest = (self.interest * self.balance)
       self.transactions.append(f"Interest: ${interest}")
       return interest
    
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
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'transactions':
        report = atm.print_transactions()
        print(f"transactions: {report}")

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')

    elif command == 'exit':
        break

    else:
        print('Command not recognized')
