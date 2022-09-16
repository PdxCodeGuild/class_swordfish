from enum import EnumMeta
import re
# fruits = {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75, 'cherries': 0.75}

# def value_to_key(dictionary, search_value):
#     results = []
#     for key in dictionary.keys():
#         if dictionary[key] == search_value:
#             results.append(key)
#     return results

# print(value_to_key(fruits, .75))

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

start_keys = lines[0]
keys = start_keys.split(",")                        #this creates a dictionary with Keys:value of None
contact_dict = dict(zip(keys, [None]))
# contact_dict = dict(zip(keys, [None]*len(keys)))
# print(contact_dict)

# split_lines = []
for line in lines[1::1]: 
    split_lines = line.split(",")
    # print(split_lines)

# line = ['Gage', 'apple', 'blue']
for i, key in enumerate(keys):
    contact_dict[key] = split_lines[i]
    print(contact_dict)
    



#     # if keys[i] == split_lines[i]:
#     #     contact_dict[keys[i]].append(split_lines[i])
    



# print(contact_dict)




# seperated_vals = [{key : lines[key] for key in range(0, len(lines))}]



    

