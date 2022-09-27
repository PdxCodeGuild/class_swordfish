"""I think to make this work you need to split lines into seperate lists and then zip them"""
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
    #new_lists = [lines[x:x+1] for x in range(0, len(lines), 1)] #[['name,favorite color,favorite fruit'], ['bob,green,cherry'], ['julia,yellow,pineapple'], ['manny,red,apple'], ['debby,purple,kiwi'], ['']]
    new_lists = [line.split(',') for line in lines] #make lists of strings
    print(new_lists)

#     del new_lists[-1] #removes last list ['']
#     #print(new_lists)
# """Now we need a function that will pull each list out and then zip it to the first list (so pop out first list w/ new variable) in a loop / list comprehension. End result is a list of seperate dictionaries"""
# headers = new_lists.pop(0) #pop out first list
# print(new_lists) #[['bob,green,cherry'], ['julia,yellow,pineapple'], ['manny,red,apple'], ['debby,purple,kiwi']]

# # zipped = zip(*new_lists)
# # zipped_list = list(zipped)
# print(zipped_list)
#print(new_lists)
#contact_lists = dict()
#for sublist in new_lists:
    #contact_lists[tuple(sublist[:3])] = [tuple(sublist[:3])] 
# for list in new_lists:
#     contact_lists = list.rstrip()
# for sublist in new_lists:
#     contact_lists.pop(0)
#     print(contact_list)
#for list in new_lists:
#     #contact_list = dict(zip(headers, new_lists))
#     contact_list = zip(headers, new_lists)
