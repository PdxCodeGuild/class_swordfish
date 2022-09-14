#Mob Programming: Jackalope Simulator

import random

#birth function to return newborn jackalope info
def birth(sex = None):
    jack_dict = {
        # 'name': not sure how to approach this
        'age': 0, 
        'sex': random.choice(['Male', 'Female']),
        'pregnant': False
    }
    return jack_dict

#population = [{'age': 0, 'sex': 'Male', 'pregnant': False}, {'age': 0, 'sex': 'Female', 'pregnant': False}] # jackalopes are stored as dict in list
population = [birth() for i in range(6)]
year = 0

#returns list of all newborn dictionaries
def pop_increase():
    jack = []
    for i in population: 
        if i['pregnant'] == True:
            jack.append(birth())
    return jack

#sets pregnancy status for females
def sex():
    for i in range(len(population)):
        if population[i]['sex'] == 'Female':
            #checks if next to male jackalope (connects list ends)
            if population[(i + 1) % len(population)]['sex'] == 'Male' or population[(i - 1) % len(population)]['sex'] == 'Male':
                population[i]['pregnant'] = True
            

#each loop iteration is 1 year
while len(population) < 7:
    for i in range(len(population)):
        population[i]['age'] += 1 #jackalope ages 1 year
    sex()
    population.append(birth())

# print(population)
# print(len(population))
print([[population[i]['sex'], population[i]['pregnant']] for i in range(len(population))])