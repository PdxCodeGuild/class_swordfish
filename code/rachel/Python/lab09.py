class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.1
    
    def check_balance(self):
        """Returns the account balance"""
        return f"{self.balance}"

    def deposit(self, amount):
        """Deposits the given amount in the account"""
        self.new_balance = amount + self.balance
        #return f"{amount}"
        return amount
        
    def check_withdrawal(self, amount):
        """Returns true if the withdrawn amount won't put the account in the negative"""
        amount -= self.new_balance

    def withdraw(self, amount):
        """Withdraw the amount from the account and returns it"""
        #self.remaining_balance = self.new_balance - amount
        return amount

    def calc_interest(self):
        """Returns the amount of the interest calculated on the account"""
        self.earned_interest = self.new_balance * self.interest_rate
        return self.earned_interest

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
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')