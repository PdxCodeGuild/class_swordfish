import requests
import pprint
import json

response = requests.get('https://favqs.com/api/qotd', headers = {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

#random_quote = json.loads(response.text)['quote']['body']
#author = json.loads(response.text)['quote']['author']
#data = response.json()
#pprint.pprint(data)
#print(random_quote, "--", author)



#Version 2 
while True:
    
    keyword = input("Please enter keyword to search for quotes: ")
    my_params={'filter': keyword}
    res = requests.get('https://favqs.com/api/quotes', headers = {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = my_params)
    quotes = res.json()['quotes']
    
    
    for dic in quotes:
        for key in dic:
            if key == "body":
                print(dic[key],'\n')
    
               
    last_page = res.json()['last_page']
    print("Last page? ", last_page)
    page = res.json()['page']
    print("Page ", page)

    while last_page == False:
        next = input("To see the next page, type 'next'. To search by new keyword, please type new search term. To quit, type 'quit.'  ")
        if next == "next":
            page = res.json()['page'] + 1            
            my_params={'filter': keyword, 'page': page}
            res = requests.get('https://favqs.com/api/quotes', headers = {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = my_params)
            quotes = res.json()['quotes']
            for dic in quotes:
                for key in dic:
                    if key == "body":
                        print(dic[key],'\n')
            last_page = res.json()['last_page']
            print("Last page? ", last_page)
            page = res.json()['page']
            print("Page ", page)
                          
        elif next == 'quit':
            break
    
        
         