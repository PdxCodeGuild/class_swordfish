import random

def pick6():                                # Function producing 6 random numbers in a list between 1 and 10.
    pick6=[]
    for i in range(6):
        random_num = random.randint(1, 99)
        pick6.append(random_num)
    return pick6
win_tik = pick6()     # Use the function to generate the winning numbers.

def num_match():      # Figures out number of matching numbers on each ticket to the winning numbers.
    winning = 0
    if tik_num[0] == win_tik[0]:        
        winning += 1
    elif tik_num[1] == win_tik[1]:
        winning += 1
    elif tik_num[2] == win_tik[2]:
        winning += 1
    elif tik_num[3] == win_tik[3]:
        winning += 1
    elif tik_num[4] == win_tik[4]:
        winning += 1
    elif tik_num[5] == win_tik[5]:
        winning += 1
    return winning

balance = 0        # My money balance
num_tiks = 0       # Place holder for the number of tickets
winning_tik = 0    # Place holder for number of winning tickets
earnings = 0       # Place holder for earnings from winning tickets

while num_tiks <= 100000:        # While loop to gerate tickets and take $2 per ticket
    tik_num = pick6()           # The 6 numbers on the ticket.
    balance -= 2                # Takes the money every ticket
    num_tiks += 1               # Creates a new ticket.
    num_match()
    if num_match() > 0:         # Figures out the number of winning tickets
        winning_tik += 1
    if num_match()==1:          # Adds money to earnings for number of matching numbers
        earnings += 4
    elif num_match()==2:
        earnings += 7
    elif num_match()==3:
        earnings += 100
    elif num_match()==4:
        earnings += 50000
    elif num_match()==5:
        earnings += 1000000
    elif num_match()==6:
        earnings += 25000000


roi = (earnings - balance)/balance      # Calulates a return on investment percentage.  

print(f'You have {winning_tik} winning tickets out of 100000')     # Prints number of winning tickets

        # Prints out the end statement.
print(f'You have won ${earnings}!!\n But, your ROI is ${roi}%.\n That means your new balance is ${earnings + balance}.')