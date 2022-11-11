from bs4 import BeautifulSoup
import requests
import re
import statistics as s
import string


url = 'https://www.allrecipes.com/recipe/15183/carrot-patties/'

def start(url):
    result = requests.get(url)
    doc = result.text # html

    soup = BeautifulSoup(doc, 'html.parser')
    all_text = soup.get_text().lower()

    file_title = soup.title.string.lower()
    file_title = file_title.replace(' ', '_')
    for x in range(len(file_title)):
        if file_title[x] not in string.ascii_letters and file_title[x] != '_':
            file_title = file_title[:x - 1]
            break

    with open(f'./recipes/{file_title}.txt', 'w') as f: # save all text to file
        f.write(f'url: {url}\n' + all_text)
    
    return all_text
    # --- website body text can now be manipulated --- #

all_text = start(url) # gets text from webpage and saves file



# POSSIBLE: could analyze many recipes to approximate words most often in recipes
ingredient_keywords = ['clove', 'pinch', 'pound', 'gram', 'ounce', 'ingredients', 'cup', 'tbsp', 'tablespoon', 'tsp', 'teaspoon'] # list of keywords commonly found in ingredient list



def find_indices(part, whole): # returns all indices of given keyword
    indices = []
    hits = re.findall(part, whole)
    for hit in hits:
        index = whole.index(hit)
        indices.append(index)
        whole = whole[:index] + whole[index + len(hit):] # slices out hit in order to find index of next hit
    return indices

keyword_indices = [] 
for x in ingredient_keywords: # populates list with all indices of found keywords
    keyword_indices += (find_indices(x, all_text))
keyword_indices = sorted(keyword_indices)
print(keyword_indices)

keyword_indices_variance = []
for x in range(len(keyword_indices) - 1): # populates list with index variance from next index, representing how condensed keywords are
    variance = keyword_indices[x + 1] - keyword_indices[x]
    keyword_indices_variance.append(variance)
print(keyword_indices_variance)

keyword_indices_variance_select = []
for x in range(len(keyword_indices_variance)): # populates list with indices of hits in close proximity of eachother - indices to be used with keyword_indices list
    if keyword_indices_variance[x] < int(round(s.mean(keyword_indices_variance))):
        keyword_indices_variance_select.append(x)
print(keyword_indices_variance_select)

keyword_indices_select = []
for x in keyword_indices_variance_select: # populates list with indices of keywords expected to be in recipe
    keyword_indices_select.append(keyword_indices[x])


print(keyword_indices_select)

def largest_sequence(my_list):
    temp = []
    for x in range(len(my_list) - 1):
        if my_list[x] + 1 == my_list[x + 1] + 1:
            temp.append(my_list[x])


ingredients = all_text[keyword_indices_select[0]: keyword_indices_select[-1]]




# --------- TESTING ---------------------------------------------------------------------------------------------------





with open(f'./ingredients/temp.txt', 'w') as f: # save ingredients to file
        f.write(ingredients)

# --------- RECYCLING BIN ---------------------------------------------------------------------------------------------------

# delta_keyword_indices_variance = []
# for x in range(len(keyword_indices_variance) - 1): # populated list with change in variance
#     delta = keyword_indices_variance[x + 1] - keyword_indices_variance[x]
#     delta_keyword_indices_variance.append(delta)
# print(delta_keyword_indices_variance)



# all_text_ref = ''
# for line in all_text_ref.splitlines(): # removes empty lines
#     if line != '':
#         all_text_ref += line + '\n'
