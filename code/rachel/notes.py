#Compute Automated Readability Index
# Save a text file containing the Gettysburg Address (copied from internet)
    #copy just text into a .txt file
# Open the file in python
# Seperate the file into a few different lists:
    # Characters
    # Words
    # Sentences (find & count periods)
# Count the number of each (return len)
# Compute the ARI using the formula in the lab instructions
# Copy dicitonary into code and compare ARI output against it
# Print output message

filename = 'gettysburg.txt'
# f = open('gettysburg.txt')
# contents = f.read()

#print(contents)

with open(filename) as gettysburg_file:
    lines = gettysburg_file.readlines() #prints out list containing each sentence (or until return / new paragraph) as an element of the list
    #sentences = lines.count(".") #this just returned 0; try it with the "for line...""
    #print(sentences)
# for line in lines:
#     print(line.rstrip()) #returns string of contents exactly as they look in text doc
#     words = line.split() #returns list of individual words as elements of list, one list for each return / paragraph
#     print(words)

#do i need to run this as function?
# def word_list():
#     for line in lines:
#         text_string = line.rstrip()
#         return text_string

# or can I just run the original with/for operation without having to print/return line.rstrip? >>> this works, returning 3 lists for the three paragraphs of the original text
for line in lines:
    text_string = line.rstrip() #returns string of contents exactly as they look in text doc
    words = line.split() #returns list of individual words as elements of list, one list for each return / paragraph
    #print(words)
    #print(len(words)) # returns 30 72 162, each on their own line
    word_count = len(words) # w/ print(word_count), returns 30 72 162, each on their own line
    print(word_count)

#turning above into a function in order to turn output (word_count) into a list:
def number_of_words():
    for line in lines:
        text_string = line.rstrip() #returns string of contents exactly as they look in text doc
        words = line.split() #returns list of individual words as elements of list, one list for each return / paragraph
        #print(words)
        #print(len(words)) # returns 30 72 162, each on their own line
        word_count = len(words) # w/ print(word_count), returns 30 72 162, each on their own line
        return word_count
total_words = []
for i in total_words:
    word_count = number_of_words()
    total_words.extend(word_count)
    print(total_words)

total_words = []
for i in total_words:
    word_count = number_of_words()
    #total_words.extend(word_count)
    total_words.append(word_count)
print(total_words)

# or to return a list
def number_of_words():
    #total_words = 0
    total_words_list = []
    for line in lines:
        text_string = line.rstrip()
        words = line.split()
        word_count = len(words) 
        #total_words += word_count
        total_words_list.append(word_count)
    return total_words_list

#trying to use len to count all the characters in the text (kept returning "char_count = len((ele for ele in text_string if ele.isalpha())) TypeError: object of type 'generator' has no len()" )
# #return letter count
# for line in lines:
#     text_string = line.rstrip()
#     char_count = len((ele for ele in text_string if ele.isalpha())
#     print(char_count)


#turn word_count output into a list IOT sum the elements
# word_count = [] 
# for i in word_count:
#     word_count.append(i)
# print(word_count)
# total_words = 0
# for i in word_count:
#     total_words += i
# print(total_words)
# for words in filename:
#     text_string = word_list()
#     print(text_string) #just returns first sentence as a string
#print(word_list()) #outside function just returns first sentence as a string
#words = line.split() # returns"NameError: name 'line' is not defined. Did you mean: 'lines'?""
# words = word_list.split() #returns "AttributeError: 'function' object has no attribute 'split'"
# print(words)

#return word count:
# for line in lines:
#     text_string = line.rstrip()
#     words = line.split()
#     word_count = len(words)
#     print(word_count) returns 30 72 162, each on their own line

#turn word_count output into a list IOT sum the elements
# word_count = [] 
# for i in word_count:
#     word_count.append(i)
# print(word_count)

# total_words = 0
# for i in word_count:
#     total_words += i
# print(total_words)

# count the words in each list and return sum of all three:
# total_words = 0
# for line in lines:
#     text_string = line.rstrip()
#     words = line.split()
#     word_count = len(words) 
#     total_words += word_count
# print(total_words) 

