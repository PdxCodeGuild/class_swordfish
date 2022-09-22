import math
class ATM():                
    def __init__(self):             # In initializer put balance, interest rate, and placeholder for transactions.
        self.__balance = 0
        self.interest = 0.001
        self.transactions = []
        
    def check_balance(self):        # Returns current balance when called.
        self.transactions.append(f'Check balance: ${self.__balance}')
        return round(self.__balance, 2)     # Added in the round() function to prevent the float storage giving an infinite decimal.
    
    def deposit(self, amount):      # Takes amount input from user and adds it to current balance.
        self.transactions.append(f'Deposit: ${amount}')
        self.__balance += amount
    
    def check_withdrawal(self, amount): # Check function to ensure you don't overdraw the account.
        return self.__balance >= amount
          
    def withdraw(self, amount):     # Takes amount input from user and subtracts it from current balance.
        self.transactions.append(f'Withdrawal: ${amount}')
        self.__balance -= amount

    def calc_interest(self):        # When called by user, calculated interest on current balance rounded to two digits.
        interest = round(self.__balance * self.interest, 2) # Code in while loop adds it to the balance.
        self.transactions.append(f'Checked interest: ${interest}') # I wish this is the way it worked in real life!!!!!!!!!!
        return interest

    def print_transactions(self):   # Pulls current transaction list when user asks.
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
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get a list of transactions') # Add transactions into the help list.
        print('exit - exit the program')
    elif command == 'transactions':
        trans = atm.print_transactions() # call the print_transactions() method.
        print(f'Transactions:\n{trans}')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')