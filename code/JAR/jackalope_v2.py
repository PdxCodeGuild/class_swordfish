#Mob Programming: newbornsalope Simulator

import random
import matplotlib.pyplot as plt
import numpy as np

#birth function to return newborn newbornsalope info
def birth():
    newborn = {
        # 'name': not sure how to approach this
        'age': 0, 
        'sex': random.choice(['Male', 'Female']),
        'pregnant': False
    }
    return newborn

population = [{'age': 0, 'sex': 'Male', 'pregnant': False}, {'age': 0, 'sex': 'Female', 'pregnant': False}] # newbornsalopes are stored as dict in list
# population = [birth() for i in range(3)]
year = 0

#returns list of all newborn dictionaries
def pop_increase():
    newborns = []
    for i in population: 
        if i['pregnant'] == True:
            newborns.append(birth())
        i['pregnant'] = False
    return newborns

# Age check for females
def age_check(i):
    if 4 <= population[(i) % len(population)]['age'] <= 8:
        return True
    else:
        return False

# Age check for males
def male_check(i):
    if age_check(i + 1) or age_check(i - 1):
        return True
    else:
        return False

#sets pregnancy status for females
def mate():
    for i in range(len(population)):
        if age_check(i) == False:
            continue
        if population[i]['sex'] == 'Female':
            #checks if next to male newbornsalope (connects list ends)
            if population[(i + 1) % len(population)]['sex'] == 'Male' or population[(i - 1) % len(population)]['sex'] == 'Male':
                if male_check(i) == True:
                    population[i]['pregnant'] = True

# Death function removes all newbornsalopes at the age of 10.
def death():
    pop_new = list(reversed(sorted(population, key=lambda d: d['age']))) # Sorts through the list of population and puts the oldest at the front.
    for i in range(len(pop_new)):  # Runs through the new list and removes anything with above the death age.
        if pop_new[0]['age'] == 10:
            pop_new.pop(0)
    return pop_new

pop_r_total = []
pop_r_males = []
pop_r_females = []
def census(population):
    males = 0
    females = 0
    for i in population:
        if i['sex'] == 'Male':
            males += 1
        else:
            females += 1
    return ((males, females))


#each loop iteration is 1 year
while len(population) < 1000:
    for i in range(len(population)):
        population[i]['age'] += 1 #newbornsalope ages 1 year

    # population data for this year is stored
    census_year = census(population)
    pop_r_total.append(sum(census_year))
    pop_r_males.append(census_year[0])
    pop_r_females.append(census_year[1])

    population.extend(pop_increase())
    mate()
    
    population = death()
    year +=1
    

    random.shuffle(population)
    if len(population) == 0:
        print('Everyone is dead!')
        break


# setting variables to plot
plt.plot(pop_r_total, 'm', marker = 'o', label = 'total')
plt.plot(pop_r_males, 'r', marker = 'o', label = 'males')
plt.plot(pop_r_females, 'b', marker = 'o', label = 'females')
plt.legend(loc = "upper left")
plt.xlabel('Year')
plt.ylabel('Population')

plt.show() # creates plot to show data

print(f'years: {year}')
