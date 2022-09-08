'''feet = int(input("What is the distance in feet? "))
meters = feet * 0.3048
print(feet,"feet is",float(meters), "meters")
'''

distance = int(input("What is the distance?"))
units = input("What are the units?")
if units == "meters":
    meters = distance
elif units == "feet":
    meters = distance * .3048
elif units == "miles":
    meters = distance / 1609
elif units == "kilometers":
    meters = distance * 1000


print(int(distance),units,"equals",meters,"meters")



