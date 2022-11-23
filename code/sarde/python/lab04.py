'''Lab 4: Pick6
'''
'''
-Have the computer play pick6 many times and determine net balance.
-Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.
-A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket
    -and the winning numbers determines the payoff
-Order matters
- Calculate your net winnings (the sum of all expenses and earnings).
        -a ticket costs $2
        -if 1 number matches, you win $4
        -if 2 numbers match, you win $7
        -if 3 numbers match, you win $100
        -if 4 numbers match, you win $50,000
        -if 5 numbers match, you win $1,000,000
        -if 6 numbers match, you win $25,000,000
'''
'''Steps
1.Generate a list of 6 random numbers representing the winning tickets
2.Start your balance at 0
3.Loop 100,000 times, for each loop:
4.Generate a list of 6 random numbers representing the ticket
5.Subtract 2 from your balance (you bought a ticket)
6.Find how many numbers match
7.Add to your balance the winnings from your matches
8.After the loop, print the final balance'''

import random
counter = 0
balance = 0
while (counter) <= 100000:
    balance = balance - 2
    counter = counter + 1
    winning_ticket_list = []
    ticket_list = []
    n = 6
    for i in range(n):
        random_integer = random.randint(1, 99)
        random_integer_two = random.randint(1, 99)
        winning_ticket_list.append(random_integer)
        ticket_list.append(random_integer_two)
    # print(winning_ticket_list)
    # print(ticket_list)

    matching_numbers = 0
    if winning_ticket_list[0] == ticket_list[0]:
        matching_numbers = matching_numbers + 1
    if winning_ticket_list[1] == ticket_list[1]:
        matching_numbers = matching_numbers + 1
    if winning_ticket_list[2] == ticket_list[2]:
        matching_numbers = matching_numbers + 1
    if winning_ticket_list[3] == ticket_list[3]:
        matching_numbers = matching_numbers + 1
    if winning_ticket_list[4] == ticket_list[4]:
        matching_numbers = matching_numbers + 1
    if winning_ticket_list[5] == ticket_list[5]:
        matching_numbers = matching_numbers + 1

    if matching_numbers == 1:
        balance = balance + 4
    if matching_numbers == 2:
        balance = balance + 7
    if matching_numbers == 3:
        balance = balance + 100
    if matching_numbers == 4:
        balance = balance + 50000
    if matching_numbers == 5:
        balance = balance + 1000000
    if matching_numbers == 6:
        balance = balance + 25000000
print(balance)
