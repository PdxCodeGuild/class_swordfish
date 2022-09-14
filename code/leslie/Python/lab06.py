
def rot13(input_string, rotation=13): #Made rotation an argument so it can be changed
    abc = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    
    for char in input_string: #Loop through each character in string given by user
        print("Char: ", char)
        input_index = abc.find(char)
        print("Index: ", input_index)
        output_index = (input_index - rotation)
        #output_index = (input_index + rotation) % 26 --ALSO works.
        print(output_index)
        output += abc[output_index] #finds and returns index of the substring                           
    return output

input_string = input("Please enter a string: ").lower() #Change it to all lower right away

print(rot13(input_string))

        

   
         


