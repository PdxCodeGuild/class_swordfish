# Code cifer and decifer

# Second half use minus 13 ranther than + 13 to get the same results without going out of range on the list.
# alf is the varible storing the alphabet
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

code = input('Please type your message: ')  # Prompt for message you would like to put into code.
rot = int(input('Please enter rotation number (1-26): '))
code = list(code)       # Convert it to a list.

final = []                                  # Version 2 - Allows the user to input the number ROT#.
for i in code:
    if i in alf:
        ind = [alf[(alf.index(i) + rot) % len(alf)]]
        final.extend(ind)

# final = [alf[(alf.index(i) + rot) % len(alf)]for i in code if i in alf]   # Used this to lab to practice list comprehensions.

'''
        *** Original code from version 1 ***
# final = []                      # Final list place holder for what it spits out.
# for i in range(len(code)):      # For loop to loop through code to be scrambled
    # ind = alf.index(code[i])    # Code referencing alf for the alphabet index.
    # if ind < 13:                    # If in the first half of the alphabet...
    #     final.append(alf[ind + 13]) # Add 13 to the index place.
    # else:                           # If in the second half of the alphabet...
    #     final.append(alf[ind - 13]) # Subtract 13 to the index place
'''
final = ''.join(final)          # Converts is back to a str.

print(final)                    # It gets appended to the final list and printed as the scrambled message.