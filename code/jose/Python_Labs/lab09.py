
class ATM():    
    def __init__(self):
        self.balance = 0
        self.interest = 0.001
        self.transactions = []

    def calc_interest(self):
        ret = round(self.balance + self.balance * self.interest, 2)
        self.transactions.append(f'User calculated interest: ${ret}')
        return ret

    def check_balance(self):
  
        self.transactions.append(f'User checked balance: ${self.balance}')
        return self.balance


    def deposit(self, amount):
        self.transactions.append(f'User deposited ${amount}')
        self.balance += amount

    def print_transactions(self):
        
        for line in self.transactions:
            print(line)
        
    def check_withdrawal(self, amount):
        return self.balance > amount

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.transactions.append(f'User withdrew ${amount}')
            self.balance -= amount
            return amount
        else:
            self.transactions.append(f'User cannot withdraw ${amount}')            
            return 'Not enough funds.'
 


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
        print( 'history')
        print('exit     - exit the program')
    elif command == 'history':
        amount = atm.print_transactions()
        print(amount)
    elif command == 'exit':
        break
    else:
        print('Command not recognized')