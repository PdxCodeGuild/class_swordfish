# Code cifer and decifer

# Second half use minus 13 ranther than + 13 to get the same results without going out of range on the list.
# alf is the varible storing the alphabet
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

code = input('Please type your message: ')  # Prompt for message you would like to put into code.

code = list(code)       # Convert it to a list.

final = []                      # Final list place holder for what it spits out.
for i in range(len(code)):      # For loop to loop through code to be scrambled
    ind = alf.index(code[i])    # Code referencing alf for the alphabet index.
    if ind < 13:                    # If in the first half of the alphabet...
        final.append(alf[ind + 13]) # Add 13 to the index place.
    else:                           # If in the second half of the alphabet...
        final.append(alf[ind - 13]) # Subtract 13 to the index place

final = ''.join(final)          # Converts is back to a str.

print(final)                    # It gets appended to the final list and printed as the scrambled message.