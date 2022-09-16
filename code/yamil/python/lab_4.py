import random

def pick6(x):
    for num in range(6):



wt = [] #winning ticket

for num in range(6):
    wt.append(random.randint(1,99))

print(wt)

# ----------------------------------------

balance = 0
match = 0

for picks in range(100000):
    pt = [] # player ticket
    for ind_nums in range(6):
        pt.append(random.randint(1,99))
        for pick_match in range(len(pt)):
            if wt == pt:
                balance += 25000000