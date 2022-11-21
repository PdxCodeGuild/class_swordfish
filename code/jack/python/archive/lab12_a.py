from bs4 import BeautifulSoup
import requests
import re
import statistics as s
import string
import os

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://wkhtmltopdf.org/


url = input('enter url: ')

def get_doc(url):
    result = requests.get(url)
    doc = result.text
    return doc

def get_soup(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    with open('check_soup.txt', 'w') as f:
        f.write(str(soup))
    return soup

def save(doc, soup):
    
    def save_file(body, file_nametag):
        with open(f'./{file_nametag}_check.txt', 'w') as f: # save ingredients to file
            f.write(body)
    
    save_file(doc, 'html') # saves html
    save_file(str(soup), 'soup') # saves soup


doc = get_doc(url)
soup = get_soup(doc)
save(doc, soup)