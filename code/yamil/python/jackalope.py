
jackalopes = [0,0]

years_passed = 0

while len(jackalopes) <= 1000:

    for x in jackalopes:  #birth
        if x >= 4 and x <= 8:
            jackalopes.append(0)

    for i in range(len(jackalopes)): #adding age
        jackalopes[i] += 1

    for item in jackalopes[:]:  #removing jackalopes after death
        if item >= 10:
            jackalopes.remove(item)

    years_passed += 1
print(jackalopes)

print(f"{years_passed} years have passed.")

