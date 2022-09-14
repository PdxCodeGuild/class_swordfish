jackalope_list = [0, 0] #both elements account for TWO Jackalopes
years = 0

while len(jackalope_list) < 1001:
    
    # print(jackalope_list)
    years += 1 
  
    for i, age in enumerate(jackalope_list):
        # print(str(i) + ' ' + str(age))
        if jackalope_list[i] >= 4 and jackalope_list[i] <= 8:
            jackalope_list.append(0)
        elif jackalope_list[i] >= 10:
            jackalope_list.pop(i)
    #jackalope_list = [x+1 for x in jackalope_list]
    
    for i in range(len(jackalope_list)):
        jackalope_list[i] = jackalope_list[i] + 1
    
    print(jackalope_list)

print(years)


# def jackalope_age(age):
#     begin_age = 0

#     for num in age:
#         begin_age += 1
#     return begin_age

# print(jackalope_age(age))