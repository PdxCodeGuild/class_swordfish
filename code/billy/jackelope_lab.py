'''
program: jackelope_lab 
author: billy frick
date: 20 september 2022

function:   > this program will use a list to represent a jackelope population.
            > the list will gain 2 new ints (newborns) for the jackelopes between the ages of 4 and 8.
            > every jackelope that reaches 10 will be removed from the list (via .pop())
            > years will be tracked for each instance of the while loop.
            > the current population and years taken to reach it will be printed.
'''

# this will store the amount of years that have passed
years_passed = 0

# bonus variable to keep track of how many jackelopes passed away.
# it seems as though 1 jackelope dies in a single year that passes.
jackelope_deaths = 0

# initial jackelope population is 2, and this is the list containing 2 ints to represent their age.
jackalopes_population = [0,0]

# this loop will continue until the jackelope population reaches 1000 (or greater).
while len(jackalopes_population) < 1000:

    # for each jackelope that is between 4 and 8, 2 more jackelopes will be added to the population list
    for jackalope in jackalopes_population:

        if 4 <= jackalope <= 8:

            # adds 2 additional jackelope for each mating instance. Start at 0 to represent them being newborns.
            jackalopes_population.append(0)
            jackalopes_population.append(0)

    # this targets the last sequence in the list to account for any jackelope that is 10 years old.
    for i in range(len(jackalopes_population)-1, -1, -1):

        # first step to removing any jackelope older than 9. when jackelope age == 10.
        if jackalopes_population[i] == 10:

            jackelope_deaths += 1

            # this removes the jackelope from the list, and sends them to jackelope heaven.
            jackalopes_population.pop(i)

    # this will 'age' each int in jackelope_population for every instance of the while loop.
    for i in range(len(jackalopes_population)):

        jackalopes_population[i] += 1

    # adds +1 to variable 'years_passed' to store until the population reaches 1000.
    years_passed += 1

# prints the number of years passed.
print(f"\n> {years_passed} years have passed ({jackelope_deaths} jackelopes passed away in that time).")

# prints the current jackelope population.
print(f"\n> the current jackelope population is {len(jackalopes_population)}.\n")

