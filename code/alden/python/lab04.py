import random

def pick6():                                # Function producing 6 random numbers in a list between 1 and 10.
    pick6=[]
    for i in range(6):
        random_num = random.randint(1, 10)
        pick6.append(random_num)
    return pick6
win_tik = pick6()                           # Use the function to generate a winning ticket.

def num_match():                            # Figures out number of matchs in a ticket
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

balance = 0                                 # My money balance
num_tiks = 0                                # Place holder for the number of tickets
winning_tik = 0

while num_tiks < 100000:                    # While loop to gerate tickets and take $2 per ticket
    tik_num = pick6()                       # The 6 numbers on the ticket.
    balance -= 2                            # Takes the money every ticket
    num_tiks += 1                           # Creates a new ticket.
    num_match()
    if num_match() > 0:         # Figures out the number of winning tickets
        winning_tik += 1
    if num_match()==1:          # Adds money to balance for number of matching numbers
        balance += 4
    elif num_match()==2:
        balance += 7
    elif num_match()==3:
        balance += 100
    elif num_match()==4:
        balance += 50000
    elif num_match()==5:
        balance += 1000000
    elif num_match()==6:
        balance += 25000000
    
    
    # print(num_match())
    # print(tik_num)

# print(win_tik)
print(f'{winning_tik} winning tickets')     # Prints number of winning tickets
print(f'${balance}')                        # Prints final balance