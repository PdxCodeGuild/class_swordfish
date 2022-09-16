'''
program: lab_04
author: billy frick
date: 12 september 2022

funcion: this program will generate 6 random numbers as the "winning numbers". The net winnings will be printed out at the end.

'''
import random

# the program rarely returns matching numbers, for some reason.

# this function will compare each element in both lists, and add +1 to the variable 'matching_numbers'
def ticket_comparison(winning_numbers, generated_tickets):

    matching_numbers = 0
    
    for i in range(6):

        if winning_numbers[i] == generated_tickets[i]:

            matching_numbers += 1

    return matching_numbers

# this function generates a 6-digit ticket at random. This will be used for the winning ticket, as well as any generated tickets.
def ticket_randomizer():

    ticket_numbers = []

    start = 0

    stop = 6

    # selects a random number between 1 and 99 to loop 6 times for the ticket numbers.
    while start < stop:

        number = random.randint(1 , 99)

        ticket_numbers.append(number)

        start += 1

    return ticket_numbers
    
# defined variables    
expenses = 0

earnings = 0

ticket_generator = 0

winning_numbers = ticket_randomizer()

generated_tickets = ticket_randomizer()

number_of_matches = ticket_comparison(winning_numbers, generated_tickets)

# this will run the program 100000 times, creating 100000 tickets to compare to the winning ticket.
while ticket_generator < 100000:

    ticket_generator += 1

    generated_tickets = ticket_randomizer()

    expenses += 2

# if/elif to add the amount earned for each generated ticket number that matches the winning numbers.
if number_of_matches == 1:
    earnings += 4

elif number_of_matches == 2:
    earnings += 7

elif number_of_matches == 3:
    earnings += 100

elif number_of_matches == 4:
    earnings += 50000

elif number_of_matches == 5:
    earnings += 1000000

elif number_of_matches == 6:
    earnings += 25000000

print("\n> You have", number_of_matches, "matches")

# calculates total earnings
total_earnings = earnings - expenses

# calculates the ROI
return_on_investement = (earnings - expenses) / expenses


print("\n> Your total earnings:", total_earnings)

print("\n> your ROI is: ", return_on_investement, "\n")