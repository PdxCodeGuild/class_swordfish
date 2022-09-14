def rot13(input_string):
    abc = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    
    for char in input_string:
        output += abc[(abc.find(char) +13)%26]
    return output

input_string = input("Please enter a string: ")

print(rot13(input_string))
print(rot13(rot13(input_string)))
