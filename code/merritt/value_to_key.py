fruits = {'apple': 1.0, 'pear': 1.5, 'banana': 0.25, 'grapes': 0.75, 'cherries': 0.75}

def value_to_key(dictionary, search_value):
    results = []
    for key in dictionary.keys():
        if dictionary[key] == search_value:
            results.append(key)
    return results

print(value_to_key(fruits, .75))
