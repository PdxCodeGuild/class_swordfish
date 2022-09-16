# Unit Converter

# Version 1

#feet = input("What is the distance in feet? ")
#feet = int(feet)

#metersfeet = feet * .3048
#metersfeet = float(metersfeet)

#print(f"{feet} ft is {metersfeet} m")

# Version 2 & 3

# distance = input("What is the distance? ")
# distance = float(distance)

# unit = input("What are the units? ")

# ft = .3048
# mi = 1609.34
# m = 1.0
# km = 1000.0
# yd = .9144
# inch = .0254

# if unit == "feet":
#     meters = distance * ft
#     print(f"{distance} ft is {meters} m")
# elif unit == "miles":
#     meters = distance * mi
#     print(f"{distance} mi is {meters} m")
# elif unit == "meters":
#     meters = distance * m
#     print(f"{distance} m is {meters} m")
# elif unit == "kilometers":
#     meters = distance * km
#     print(f"{distance} km is {meters} m")
# elif unit == "yards":
#     meters = distance * yd
#     print(f"{distance} yd is {meters} m")
# elif unit == "inches":
#     meters = distance * inch
#     print(f"{distance} in is {meters} m")

# Version 4

distance = input("What is the distance? ")
distance = float(distance)

inputunit = input("What are the input units? ")

output = input("What are the output units? ")


if output == "feet":
    output = .3048
    outputunit = "ft"
elif output == "miles":
    output = 1609.34
    outputunit = "mi"
elif output == "meters":
    output = 1.0
    outputunit = "m"
elif output == "kilometers":
    output = 1000.0
    outputunit = "km"


ft = .3048
mi = 1609.34
m = 1.0
km = 1000.0


if inputunit == "feet":
    meters = distance * ft
    conversion = meters / output
    conversion = float(conversion)
    print(f"{distance} ft is {conversion} {outputunit}")
elif inputunit == "miles":
    meters = distance * mi
    conversion = meters / output
    conversion = float(conversion)
    print(f"{distance} mi is {conversion} {outputunit}")
elif inputunit == "meters":
    meters = distance * m
    conversion = meters / output
    conversion = float(conversion)
    print(f"{distance} m is {conversion} {outputunit}")
elif inputunit == "kilometers":
    meters = distance * km
    conversion = meters / output
    conversion = float(conversion)
    print(f"{distance} km is {conversion} {outputunit}")
