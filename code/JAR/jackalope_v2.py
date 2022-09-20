#Mob Programming: Jackalope Simulator

import random
import re

#birth function to return newborn jackalope info
def birth():
    jack_dict = {
        # 'name': not sure how to approach this
        'age': 0, 
        'sex': random.choice(['Male', 'Female']),
        'pregnant': False
    }
    return jack_dict

population = [{'age': 0, 'sex': 'Male', 'pregnant': False}, {'age': 0, 'sex': 'Female', 'pregnant': False}] # jackalopes are stored as dict in list
# population = [birth() for i in range(3)]
year = 0

#returns list of all newborn dictionaries
def pop_increase():
    jack = []
    for i in population: 
        if i['pregnant'] == True:
            jack.append(birth())
        i['pregnant'] = False
    return jack

# Age check for females
def age_check(i):
    if 4 <= population[i]['age'] <= 8:
        return True
    else:
        return False

# Age check for males
def male_check(i):
    if 4 <= population[(i + 1) % len(population)]['age'] <= 8 or 4 <= population[(i - 1) % len(population)]['age'] <= 8:
        return True
    else:
        return False

#sets pregnancy status for females
def sex():
    for i in range(len(population)):
        if age_check(i) == False:
            continue
        if population[i]['sex'] == 'Female':
            #checks if next to male jackalope (connects list ends)
            if population[(i + 1) % len(population)]['sex'] == 'Male' or population[(i - 1) % len(population)]['sex'] == 'Male':
                if male_check(i) == True:
                    population[i]['pregnant'] = True

# Death function removes all jackalopes at the age of 10.
def death():
    pop_new = list(reversed(sorted(population, key=lambda d: d['age']))) # Sorts through the list of population and puts the oldest at the front.
    for i in range(len(pop_new)):  # Runs through the new list and removes anything with above the death age.
        if pop_new[0]['age'] == 10:
            pop_new.pop(0)
    return pop_new

#each loop iteration is 1 year
while len(population) < 1000:
    for i in range(len(population)):
        population[i]['age'] += 1 #jackalope ages 1 year
    sex()
    year +=1
    population.extend(pop_increase())
    population = death()
    random.shuffle(population)
    if len(population) == 0:
        print('Everyone is dead!')
        break

# print(death())
# print(len(population))
# print([[population[i]['sex'], population[i]['pregnant'], population[i]['age']]for i in range(len(population))])
print(year)
# print(death_num)