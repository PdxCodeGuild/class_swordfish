'''
program: lab_04
author: billy frick
date: 12 september 2022

funcion: this program will generate 6 random numbers as the "winning numbers". The net winnings will be printed out at the end.

'''

import random

def ticket_comparison(winning_numbers, generated_tickets):

    matching_numbers = 0

    for i in range(len(winning_numbers)):

        if winning_numbers[i] == generated_tickets[i]:

            matching_numbers += 1

    return matching_numbers

# this function generates a 6-digit ticket at random. This will be used for the winning ticket, as well as any generated tickets.
def ticket_randomizer(ticket_numbers):

    ticket_numbers = []

    start = 0

    stop = 6

    # selects a random number between 1 and 99 to loop 6 times for the ticket numbers.
    while start < stop:

        number = random.randint(1 , 99)

        ticket_numbers.append(number)

        start += 1

    return ticket_numbers
    
expenses = 0

earnings = 0

ticket_generator = 0

winning_numbers = []

generated_tickets = []

print("\nThe winning numbers are:", ticket_randomizer(winning_numbers))

number_of_matches = ticket_comparison(winning_numbers, generated_tickets)

print("The number of matches is:", number_of_matches)

# this will run the program 100000 times, creating 100000 tickets to compare to the winning ticket.
while ticket_generator < 100000:

    expenses += 2

    (ticket_randomizer(generated_tickets))

    ticket_generator += 1

print(earnings, expenses)
