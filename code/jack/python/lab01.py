#Lab 01 Unit Converter

distance_input = float(input("What is the distance? "))
unit_input = input("What unit are you converting from? ")
unit_output = input("What unit are you converting to? ")

conversion_dict = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000    
}

#convert from UNIT to m
for x in conversion_dict:
    if unit_input == x:
        distance_m = distance_input * conversion_dict[x]

for x in conversion_dict:
    if unit_output == x:
        distance_output = distance_m / conversion_dict[x]

print(f"{distance_input} {unit_input} is equal to {distance_output} {unit_output}")