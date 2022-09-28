import requests
import json
import pprint

#-----------------------------------------------------

# response = requests.get("https://favqs.com/api/qotd")


# quote_dict = response.json()
# print(quote_dict["quote"]['body'],"\n",quote_dict["quote"]['author'])

# ----------------------------------------------------

# quote_keyword = input("Enter a keyword to search for quotes: ")

# page = 1

# response = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={quote_keyword}", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

# quote_dict = response.json()

# quote_counter = len(quote_dict['quotes'])

# print(f"{quote_counter} quotes associated with '{quote_keyword}' in page {page}.","\n")

# for i in quote_dict['quotes']:
#     print(i['body'],"\n")

#-----------------------------------------------------
x=0

quote_keyword = input("Enter a keyword to search for quotes: ")

page = 1

response = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={quote_keyword}", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

quote_dict = response.json()

quote_counter = len(quote_dict['quotes'])

print(f"{quote_counter} quotes associated with '{quote_keyword}' in page {page}.","\n")

for i in quote_dict['quotes']:
    print(i['body'],"\n")

while True:
    next_or_end = input("Would you like to see 'next page' or 'end'?: ")
    if next_or_end == 'next page':
        page += 1
        response = requests.get(f"https://favqs.com/api/quotes?page={page}&filter={quote_keyword}", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        quote_dict = response.json()
        quote_counter = len(quote_dict['quotes'])
        print(f"{quote_counter} quotes associated with '{quote_keyword}' in page {page}.","\n")
        for i in quote_dict['quotes']:
            print(i['body'],"\n")
    elif next_or_end == 'end':
        break
    else:
        print("Please enter 'next page' or 'end'.")