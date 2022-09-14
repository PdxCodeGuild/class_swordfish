jackalopes = [4, 4]
years = 0

while len(jackalopes) <= 1000:

    for x in jackalopes:
        if x >= 4 and x <= 8:
            jackalopes.append(0)
    years = years + 1

    for i in range(len(jackalopes)):
        jackalopes[i] += 1


print(jackalopes)
