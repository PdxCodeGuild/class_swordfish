jackalope_list = [0, 0] #both elements account for TWO Jackalopes = Overall Jackalope Population
years = 0

while len(jackalope_list) < 1001:
    # print(jackalope_list)
    years += 1 #will keep adding 1 year to yearsvariable until population is at 1000
    for i, age in enumerate(jackalope_list):
        # print(str(i) + ' ' + str(age))
        if jackalope_list[i] >= 4 and jackalope_list[i] <= 8:
            jackalope_list.append(0)
        elif jackalope_list[i] >= 10:
            jackalope_list.pop(i)
    jackalope_list = [x+1 for x in jackalope_list] # x is the index value
    print(jackalope_list)

print(years)


# fruits = ['apples', 'bananas', 'pears']
# for i, fruit in enumerate(fruits):
#     print(str(i) + ' ' + fruit)