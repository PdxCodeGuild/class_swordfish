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

# population = [{'age': 0, 'sex': 'Male', 'pregnant': False}, {'age': 0, 'sex': 'Female', 'pregnant': False}] # jackalopes are stored as dict in list
population = [birth() for i in range(3)]
year = 0
death = 0
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
    if 1 <= population[i]['age'] <= 8:
        return True
    else:
        return False

# Age check for males
def male_check(i):
    if 1 <= population[(i + 1) % len(population)]['age'] <= 8 or 2 <= population[(i - 1) % len(population)]['age'] <= 8:
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
            

#each loop iteration is 1 year
while len(population) < 20:
    for i in range(len(population)):
        population[i]['age'] += 1 #jackalope ages 1 year
    sex()
    population.extend(pop_increase())
    for i in range(len(population)):  # *** Death function not finished yet. Still broken. ***
        if population[0]['age'] == 3:
            population.pop(0)
            death += 1
    year +=1

# print(population)
# print(len(population))
print([[population[i]['sex'], population[i]['pregnant'], population[i]['age']]for i in range(len(population))])
print(year)
print(death)