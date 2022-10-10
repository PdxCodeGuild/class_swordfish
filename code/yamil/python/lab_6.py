from base64 import decode


input_string = input("What would you like to encrypt?: ")
input_string.lower()
# user_rotation = int(input("How much rotation in the cipher?: "))

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
rot_13 = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]

output_list = [x for x in input_string]
decoded_list = []

# Once the string is entered, we need to change each individual letter to its shifted counterpart. A = N etc.

for x in output_list:
    x = alphabet.index(x)
    decoded_list.append(rot_13[x])


decoded_list = "".join(decoded_list)

print(output_list)
print(decoded_list.title())