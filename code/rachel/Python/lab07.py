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

with open(filename) as gettysburg_file:
    lines = gettysburg_file.readlines() 

#return word count:
# for line in lines:
#     text_string = line.rstrip()
#     words = line.split()
#     word_count = len(words)
#     print(word_count) returns 30 72 162, each on their own line

# #return letter count
# for line in lines:
#     text_string = line.rstrip()
#     char_count = len((ele for ele in text_string if ele.isalpha())
#     print(char_count)

#turning above into a function in order to turn output (word_count) into a list:
def number_of_words():
    total_words = 0
    #total_words_list = []
    for line in lines:
        text_string = line.rstrip()
        words = line.split()
        word_count = len(words) 
        total_words += word_count
        #total_words_list.append(word_count)
    return total_words

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

total_words = []
for i in total_words:
    word_count = number_of_words()
    #total_words.extend(word_count)
    total_words.append(word_count)
print(total_words)


#turn word_count output into a list IOT sum the elements
# word_count = [] 
# for i in word_count:
#     word_count.append(i)
# print(word_count)

# total_words = 0
# for i in word_count:
#     total_words += i
# print(total_words)







