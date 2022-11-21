"""I think to make this work you need to split lines into seperate lists and then zip them"""
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n') #returns one big list with seperate elements (notice the single quotes around 'bob,green,cherry' - it's just one big string): ['name,favorite color,favorite fruit', 'bob,green,cherry', 'julia,yellow,pineapple', 'manny,red,apple', 'debby,purple,kiwi']
    #print(lines)
    new_lists = [line.split(',') for line in lines] #turn those strings into their own list of things to work with: [['name', 'favorite color', 'favorite fruit'], ['bob', 'green', 'cherry'], ['julia', 'yellow', 'pineapple'], ['manny', 'red', 'apple'], ['debby', 'purple', 'kiwi']]
    #print(new_lists)
headers = new_lists.pop(0) #pop out first list
#print(headers) #['name', 'favorite color', 'favorite fruit']
#print(new_lists) #[['bob', 'green', 'cherry'], ['julia', 'yellow', 'pineapple'], ['manny', 'red', 'apple'], ['debby', 'purple', 'kiwi']]
"""Now we need a function that will pull each list out and then zip it to the first list (so pop out first list w/ new variable) in a loop / list comprehension. End result is a list of seperate dictionaries"""
def list_builder(funny, new_lists): #parameter names only apply to the function definition; they are simply placeholders
    local_list = []
    for list in new_lists:
        sing_dict = dict(zip(funny,list))
        local_list.append(sing_dict)
    return local_list

print(list_builder(headers, new_lists)) #this is where I tell it to use the particular lists I want it to use
"""See if user name is in dictionary and print out everything in that dictionary"""
    #print [d['name']] for d in contact_list if user_name in d]
    #    or
    # for d in contact_list:
    #     if user_name in d:
    #         fav_color = d.get('favorite color')
    #         fav_fruit = d.get('favorite fruit')
    #         print(fav_color)
    #         print(fav_fruit)
        #print(f'Your favorite color is {fav_color} and your favorite fruit is {fav_fruit}.')



"""Program below returns 5 sets of {('name', 'favorite color', 'favorite fruit'): [('bob', 'green', 'cherry')]}"""
# contact_list = {}
# def list_iter(): #return each list seperately as it goes thru loop
#     for list in new_lists:
#         return list
# for list in new_lists:
#     list = list_iter()
#     contact_list = dict(zip(headers,list)) #returns {('name', 'favorite color', 'favorite fruit'): [('bob', 'green', 'cherry')]}
#     print(contact_list)

"""adding additonal function so that it will loop through all the lists"""
# def list_iter(): #return each list seperately as it goes thru loop
#     for list in new_lists:
#         return list
# contact_list = {}
# def name_zip():
#     list = list_iter()
#     contact_list = dict(zip(headers,list))
#     return contact_list
# for list in new_lists:
#     list = list_iter()
#     contact_list = name_zip()
# print(contact_list)







#print(list_iter())

# for list in new_lists:
#     contact_lists = list.rstrip()
# for sublist in new_lists:
#     contact_lists.pop(0)
#     print(contact_list)
# contact_list = dict((k, v) for k, v in zip(headers, new_lists))
# print(contact_list)
# for list in new_lists:
#     contact_list = dict(zip(headers, new_lists))
#     #contact_list = zip(headers, new_lists) #error
#     print(contact_list)
# for sublist in new_lists:
#     contact_list[tuple(headers[:3])] = [tuple(sublist[:3])] # returns {('name', 'favorite color', 'favorite fruit'): [('bob', 'green', 'cherry')]} for each list
    #contact_list[tuple(headers[:3])] = [tuple(list[:3])] #returns {('name', 'favorite color', 'favorite fruit'): [('bob', 'green', 'cherry')]}
#     print(contact_list)