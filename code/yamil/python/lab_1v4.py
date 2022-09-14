metrics = {
"ft" : 0.3048,
"feet" : 0.3048,
"foot" : 0.3048,
"mile" : 1609.34,
"miles" : 1609.34,
"meter" : 1,
"meters" : 1,
"km" : 1000,
"kilometer" : 1000,
"kilometers" : 1000,
"yard" : 0.9144,
"yards" : 0.9144,
"inch" : 0.0254,
"inches" : 0.0254
}

distance = int(input("What is the distance?: "))
units = input("What is the unit?: ")
output = input("What is the output unit?: ")

total = distance * metrics[units]

if output != units:
    total_2 = total / metrics[output]
    print(f"{distance} {units} is equal to {total_2} {output}.")

else:
    print(f"{distance} {units} is equal to {total} {output}.")
    