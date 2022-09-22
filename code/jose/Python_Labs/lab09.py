
user_balance : (0)

class ATM():

    def __init__(self, amount, command):
        self.amount = amount
        self.command = command

    def check_balance(self):
            print(user_balance)
    
    def deposit(self, amount):
        self + user_balance
        return user_balance

    def check_withdrawal(self, amount):
        if user_balance > self:
            print('Valid, enough funds to withdraw requsted amount')
        elif user_balance < self:
            print('Invalid, not enough funds.')

    def withdraw(self):
        if user_balance > self:
            print("Here are your funds for a total of" + self)
    
    def calc_interest(self):
        user_balance * .01
        return user_balance
        


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