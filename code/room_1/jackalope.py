jackalopes = [4,4]

years_passed = 0

while len(jackalopes) <= 10:
    for x in jackalopes:
        if x >= 4 and x <= 8:
            jackalopes.append(0)

print(jackalopes)