#ARI
import math
#number of characters
file = open("myfile.txt", "r")
myfile = file.read().replace(" ","")
characters = len(myfile)
print('Number of characters in text file: ', characters)

#number of words
file = open("myfile.txt", "r")
myfile = file.read()
words = myfile.split()
print('Number of words in text file: ', len(words))

#number of sentences
with open("myfile.txt") as f:
    data = f.read()
    print ("total stops: ", data.count("."))




words = 280
characters = 1359
sentences = 11
x = 4.71
y = 21.43
z = .5

score = float(x / characters / words / + z / words / sentences / - y)

print("Score: ", score)
