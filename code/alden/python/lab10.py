# Dad joke API
'''
# from pydoc import pager
# from xml.etree.ElementInclude import LimitedRecursiveIncludeError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Can someone tell me why things like this auto import into my code while I am working on it please!!
'''
import requests

params = {}     # Place holder for the parameters in the request.get
while True:
    search = input('Please enter search peramiters(p, l, t) or help: ') # User prompt
    data = requests.get('https://icanhazdadjoke.com/search', headers = {'accept':'application/json'},  params = params)
    result = data.json()
    
    if search == "help":        # Shows all the possible inputs to the user.  Prompted to it if user doesn't input a correct command.
        print('Available searches:')
        print('p = page  (default:1)')
        print('l = limit (default:20 max:30)')
        print('t = term  (defaults: list all jokes)')
        print('pr = print jokes')
        print('e = exit')
    elif search == 'p':         # Creates a page number to search.
        p = input('What page number would you like: ')
        params.update({'page':p})
    elif search == 'l':         # Creates how many jokes you want to see.
        l = input('How many jokes would you like: ')
        params.update({'limit':l})
    elif search == 't':         # Allows to search for terms in the joke.
        t = input('Is there a term you would like: ')
        params.update({'term':t})
    elif search == 'pr':        # Prints out jokes based on the current search parameters.
        for joke in result['results']:
            print(f'{joke["joke"]}\n')
    elif search == 'e':         # Exits loop
        break
    else:
        print('Command not recognized. Enter "help" for assistance.')
        