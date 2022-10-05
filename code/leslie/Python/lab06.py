
def rot13(input_string, rotation=13): #Made rotation an argument so it can be changed
    abc = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    
    for char in input_string: #Loop through each character in string given by user
        print("Char: ", char)
        input_index = abc.find(char) #find and return the index of the input string
        print("Index: ", input_index)
        output_index = (input_index - rotation) #rotate 13 places
        #output_index = (input_index + rotation) % 26 --ALSO works.
        print(output_index)
        output += abc[output_index] #returns index of the output string                           
    return output

input_string = input("Please enter a string: ").lower() #Change it to all lower right away

print(rot13(input_string))

        

   
         


