from bs4 import BeautifulSoup
import requests
import re
import statistics as s
import string
import os

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://wkhtmltopdf.org/


url = 'https://zardyplants.com/recipes/tofu-adobo/'

def get_doc(url):
    result = requests.get(url)
    doc = result.text
    return doc

def get_soup(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    with open('check_soup.txt', 'w') as f:
        f.write(str(soup))
    return soup

def get_title(soup):
    recipe_title = soup.title.string.lower()
    recipe_title = recipe_title.replace(' ', '_')
    for x in range(len(recipe_title)):
        if recipe_title[x] not in string.ascii_letters and recipe_title[x] != '_':
            recipe_title = recipe_title[:x - 1]
            break
    return recipe_title

def get_text_recipe(soup):
    all_text = soup.get_text().lower()

    # --- website body text can now be manipulated --- #
    # # gets text from webpage and saves file

    # POSSIBLE: could analyze many recipes to approximate words most often in recipes
    # will probably need to do above to achieve sufficient accuracy
    ingredient_keywords = ['1','2','3','4','5','6','7','8','9', '¼', '⅓', '½', 'pepper', 'salt', 'to taste', 'clove', 'pinch', 'dash', 'dried', 'fresh', 'pound', ' gram', 'ounce', 'ingredients', 'cup', 'tbsp', 'tablespoon', 'tsp', 'teaspoon'] # list of keywords commonly found in ingredient list
    instruction_keywords = ['instructions', 'golden', 'brown', 'fry', 'rinse', 'preheat', 'chop', 'peel', 'add', 'transfer', 'garnish', 'mince', 'heat', 'pan', 'stir', 'sift', 'mix', 'pour', 'saute', ]

    def find_indices(part, whole): # returns all indices of given keyword
            indices = []
            hits = re.findall(part, whole)
            for hit in hits:
                index = whole.index(hit)
                indices.append(index)
                whole = whole[:index] + ''.join(['*' for _ in range(len(hit))]) + whole[index + len(hit):] # slices out hit in order to find index of next hit, fills with asterisk to maintain index integrity
            return indices

    def find_section(all_text, section_keywords): # returns all_text indices of probable ingedients

        # O(n^2), but relatively small keyword list
        keyword_indices = [] # list of all indices of keywords in all_text
        for x in section_keywords: 
            keyword_indices += (find_indices(x, all_text))
        keyword_indices = sorted(keyword_indices)
        # print(keyword_indices)

        keyword_indices_variance = [] # list of index variances from next index, representing how condensed keywords are
        for x in range(len(keyword_indices) - 1): 
            variance = keyword_indices[x + 1] - keyword_indices[x]
            keyword_indices_variance.append(variance)
        # print(keyword_indices_variance)

        # list of indices of keyword hits in close proximity of eachother
        # selects keyword indicies based on whether variance is less than the average
        keyword_indices_variance_select = []
        for x in range(len(keyword_indices_variance)): 
            if keyword_indices_variance[x] < int(round(s.mean(keyword_indices_variance))):
                keyword_indices_variance_select.append(x)
        # print(keyword_indices_variance_select)

        # function to take keyword_indices_variance_select and return longest list of consecutive indexes
        # effectively, takes the largest chunk of condensed keywords to guess at ingredients
        def largest_sequence(evaluated_list):
            storage_list = [[]] # sublists length is checked, longest sublist is kept - AKA indices of largest condensed set of keywords
            counter = 0
            for x in range(len(evaluated_list) - 1): # doesn't check last value
                storage_list[counter].append(evaluated_list[x])
                if evaluated_list[x] + 1 != evaluated_list[x + 1]:
                    storage_list.append([])
                    counter += 1
            if evaluated_list[-1] == evaluated_list[-1]: # checks last value
                storage_list[counter].append(evaluated_list[-1])

            longest_length = 0
            longest_index = 0
            for x in storage_list:
                if len(x) > longest_length:
                    longest_length = len(x)
                    longest_index = storage_list.index(x) # if storage_list contains multiple elements of same length, this stores last element
            
            return storage_list[longest_index]

        keyword_indices_variance_select = largest_sequence(keyword_indices_variance_select)

        keyword_indices_select = []
        for x in keyword_indices_variance_select: # populates list with indices of keywords expected to be in recipe
            keyword_indices_select.append(keyword_indices[x])

        # desired text is now located, but is likely missing important parts, or contains erraneous text
        # program should find common pattern throughout desired text;
        #   - is it all on one line?
        #   - is there only one space between each item? two spaces?
        # once pattern is found, recapture desired text- and compare to original desired text to see if contains mostly the same stuff



        # print(keyword_indices_select)

        # sample_out = []
        # for i in keyword_indices:
        #     sample = all_text[i:i + 10]
        #     sample_out.append(sample)
        # print(sample_out)

        return keyword_indices_select
    ingredient_keyword_indices = find_section(all_text, ingredient_keywords)
    instruction_keyword_indices = find_section(all_text[ingredient_keyword_indices[0]:], instruction_keywords) # only checks for instructions after ingredients
    instruction_keyword_indices = [x + ingredient_keyword_indices[0] for x in instruction_keyword_indices] # adjusts instruction indices given that all text before ingredients was not used
    # print(ingredient_keyword_indices[0])
    # print(instruction_keyword_indices[-1])
    select_text = all_text[ingredient_keyword_indices[0]:instruction_keyword_indices[-1]]
    
    return select_text

def save(doc, soup, recipe_title, text_recipe):
    
    def save_file(body, recipe_title, file_nametag):
        if not os.path.exists('./recipes'):
            os.makedirs('./recipes')
        if not os.path.exists(f'./recipes/{recipe_title}'):
            os.makedirs(f'./recipes/{recipe_title}')
        with open(f'./recipes/{recipe_title}/{file_nametag}_{recipe_title}.txt', 'w') as f: # save ingredients to file
            f.write(body)
    save_file(doc, recipe_title, 'html') # saves html
    save_file(get_text_recipe(soup), recipe_title, 'text') # saves extracted text
    save_file(url, recipe_title, 'url') # saves url
    save_file(text_recipe, recipe_title, 'recipe') # saves url

doc = get_doc(url)
soup = get_soup(doc)
recipe_title = get_title(soup)
text_recipe = get_text_recipe(soup)

# ! ! ! DON'T RUN - OVERWRITES RECIPE FILES ! ! !
# save(doc, soup, recipe_title, text_recipe)

# --------- TEMPORARY ---------------------------------------------------------------------------------------------------

# with open(f'./ingredients/temp.txt', 'w') as f: # save ingredients to file
#         f.write(text_recipe)

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


# with open(f'./recipes/{recipe_title}.txt', 'w') as f: # save all text to file
#     f.write(f'url: {url}\n' + all_text)