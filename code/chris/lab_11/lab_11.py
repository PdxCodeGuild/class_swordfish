import requests
import pprint

#Version 1
quote = requests.get('https://favqs.com/api/qotd', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) #headers is value of key

# print(quote.url)
# print(quote.text)
# print(quote.status_code)
# print(quote.encoding)
# print(quote.headers)

random_q = quote.json() #decode
# pprint.pprint(random_q) #print python dictionary
# body = pprint.pprint(random_q['quote']['body'])
# print(body)
# author = pprint.pprint(random_q['quote']['author'])
# the_keys = random_q.keys() 
# print('printing the keys:', the_keys) #<<<-------------------------------********************* GET KEYS TO DICT.


the_author = random_q['quote']['author']
the_body = random_q['quote']['body']
# print('the author: ', the_author)
# print('the body: ', the_body)

print(f"""VERSION 1 ANSWER:
Your random quote is: {the_body} 
- {the_author}""" + '\N') # parse dictionary to show the quote and the author

# #Version 2

# user_prompt = input('Please enter a keyword to search for quotes: ')
# # print(user_prompt)
# response = requests.get('https://favqs.com/api/quotes', params={'filter': user_prompt, 'page': 0}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b'})

print('Version 2 ANSWER: ')
while True:
    request = input('What would you like to see? ')
    # print(request)
    if request == 'keyword':
        user_prompt = input('Please enter a keyword to search for quotes: ' + '\n')
        response = requests.get('https://favqs.com/api/quotes', params={'filter': user_prompt}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b'})
        results = response.json()
        what_page = results.keys()
        # print('THIS IS THE PAGE KYS: ', what_page) THIS IS THE PAGE KYS:  dict_keys(['page', 'last_page', 'quotes'])
        quotes = results['quotes'] 
        # page = str(page)
        print(f"25 quotes associated with {user_prompt} - Page {results['page']}" + '\n')    
        for quote in quotes:  
            print(quote['body'])
            print(quote['author'] + '\n')
        # print(results['page'])
        # print(results['last_page'])
    elif request == 'next page':
        page = results['page'] + 1
        print(f"25 quotes associated with {user_prompt} - Page {page}" + '\n')
        response = requests.get('https://favqs.com/api/quotes', params={'filter': user_prompt, 'page': page}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b'})
        results = response.json() 
        quotes = results['quotes']        
        for quote in quotes:
            print(quote['body'])
            print(quote['author'] + '\n')
        # print(results['page'])
        # print(results['last_page'])
    elif request == 'help':
        print('Available commands:')
        print('keyword - uses the keyword to search for the first 25 quotes')
        print('next page - displays the next 25 quotes with the keyword')
        print('done - exit the program')
    elif request == 'done':
        break
    else:
        print('Try Again!')