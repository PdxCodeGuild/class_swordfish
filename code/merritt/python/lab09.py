# class ATM:
#     def __init__(self, balance=0, interest_rate=0.1):
#         self.__balance = balance
#         self.__interest_rate = interest_rate
#         self.__transactions = []

#     def check_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         self.__balance += amount
#         self.__transactions.append(f'user deposited ${amount}')

#     def check_withdrawal(self, amount):
#         return amount <= self.__balance

#     def withdraw(self, amount):
#         if self.check_withdrawal(amount):
#             self.__balance -= amount
#             self.__transactions.append(f'user withdrew ${amount}')
#             return amount
#         print('not enough money')

#     def calc_interest(self):
#         return self.__balance * self.__interest_rate / 100

#     def print_transactions(self):
#         return '\n'.join(self.__transactions)

class ATM:
    def __init__(self, balance=0, interest_rate=0.1):
        self.__balance = balance * 100
        self.__interest_rate = interest_rate
        self.__transactions = []

    def check_balance(self):
        return self.__balance / 100

    def deposit(self, amount):
        self.__balance += amount * 100
        self.__transactions.append(f'user deposited ${amount}')

    def check_withdrawal(self, amount):
        return amount * 100 <= self.__balance

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.__balance -= amount * 100
            self.__transactions.append(f'user withdrew ${amount}')
            return amount
        print('not enough money')

    def calc_interest(self):
        interest = self.__balance * self.__interest_rate / 100
        return interest.round() / 100

    def print_transactions(self):
        return '\n'.join(self.__transactions)


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
    elif command == 'history':
        print(atm.print_transactions())
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history - print transaction log')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')