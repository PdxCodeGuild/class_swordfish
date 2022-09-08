#Unit Converter 

distance = {
'ft' : .3048,
'm' : 1,
'mi' : 1609.34,
'km' : 1000,
'yard' : 1,
'inch' : 1
}

user = input ('What is the distance?: ')
unit_str = input('What are the units?: ')
unit_str2 = input('What are the output units?: ')

user = int(user)
unit = distance[unit_str]
results = unit * user
print(f"{user} {unit_str} is {results} {unit_str2} ")