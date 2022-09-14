#Mob Programming: Jackalope Simulator

population = [0, 0]
year = 0

while len(population) < 5:
    for i in population:
        population[i] += 1
        # if population[i] == 10:
        #     population.pop(i)
    population.append(0)
    year += 1        

print(population)
print(year)