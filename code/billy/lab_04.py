'''
program: lab_04
author: billy frick
date: 12 september 2022

funcion: this program will generate 6 random numbers as the "winning numbers". The net 

'''

import random

# def ticket_comparison(winning_numbers, generated_tickets):
    
#     matching_numbers = []

#     if generated_tickets in winning_numbers:

#         return matching_numbers



def ticket_randomizer(ticket_numbers):

    ticket_numbers = []

    start = 0

    stop = 6

    while start < stop:
        number = random.randint(1 , 99)
        ticket_numbers.append(number)
        start += 1
    return ticket_numbers
    
balance = 0

ticket_generator = 0

winning_numbers = []

generated_tickets = []

print("\nThe winning numbers are:", ticket_randomizer(winning_numbers))


while ticket_generator < 10:

    balance -- 2

    (ticket_randomizer(generated_tickets))

    # print(ticket_comparison(winning_numbers, generated_tickets))

    ticket_generator += 1

# if generated_tickets == winning_numbers:
#     balance ++ 25000000

