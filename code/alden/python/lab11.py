# Quote API

import requests

# Pulling the 'quote of the day'
qotd = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
result = qotd.json()

print(f'"{result["quote"]["body"]}" -{result["quote"]["author"]}') # Prints out the quote and the author.

# Funtcion to request data from site and print based on current search params.
def print_result():
    data = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = params)
    result = data.json()
    for i in result['quotes']:
        print(f'\n"{i["body"]}" -{i["author"]}\n')
    print(f'Page#{result["page"]}\n') # Print page number at the end of the pring out.

params = {'page': 1} # Params place holder with default page 1.
keyword = input('Please select a keyword you would like to search: ') # Asks for the initial keyword search.
params.update({'filter': keyword})  # Adds the keyword search into the params.
print_result()  # Prints initial results.

# While loop for the REPL of next page or inputing a different keyword search.
while True:
    command = input('Commnd options.\n"next" for next page,\n"keyword" for a new keyword search,\nor "done" to exit: ')

    if command == 'next':
        params['page'] += 1
        print_result()

    elif command == 'keyword':
        new = input('Please enter new keyword: ')
        params['filter'] = new
        params['page'] = 1  # Resets the page number to 1.
        print_result()

    elif command == 'done':
        break

    else:
        print('Invalid command. Please try again: ')
