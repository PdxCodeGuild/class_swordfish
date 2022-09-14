#Mob Programming: Jackalope Simulator

population = [0, 0]
year = 0

while len(population) < 15:
    for i in range(len(population)):
        population[i] += 1
    while population[0] == 5:
        population.pop(0)
    population.append(0)

    year += 1        

print(population)
print(year)