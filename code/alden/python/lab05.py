def credit_card_validator(card_num): # Function to check validation of credit card.
    x = []                          # Place holder for list to be built in.
    card_num = list(card_num)       # Converting the input to a list.
    for num in card_num:            # Loop to convert each number in the list to an int and put in place holder list.
        x.append(int(num))

    check = x.pop()                 # Pop last number and store it as a check number.
    x.reverse()                     # Reverse list.

    for i in range(0, len(x), 2):   # Take every second int and multiply by 2.
        x[i] *= 2

    for n in range(0, len(x)):      # Take any int >9 and subtract 9 from it.
        if x[n] > 9:
            x[n] -= 9

    result = 0              
    for i in x:                     # Add all int up and store under new variable result
        result = i + result

    result  = result %10            # Convert to only ones place.
    return result == check          # Return boolean on whether the result and check number are the same.

card = input('Put in your card number: ')   # Request credit card number.
card_num = credit_card_validator(card)      # Checking card number against function

print(card_num)                     # Print returned value. True = valid. False = invalid