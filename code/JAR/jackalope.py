#Mob Programming: Jackalope Simulator

population = [0, 0]
year = 0
death = 0

def pop_count():
    jack = []
    for i in population: 
        if 4 <= i <= 8:
            jack.append(0)
    return jack
while len(population) < 1000:
    for i in range(len(population)):
        population[i] += 1
    while population[0] == 10:
        population.pop(0)
        death += 1
    population.extend(pop_count())

    year += 1        

#print(population)
print(year)
print(death)