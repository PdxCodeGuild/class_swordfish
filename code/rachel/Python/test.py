# def encrypt(text,s):
# result = ""
#    # transverse the plain text
#    for i in range(len(text)):
#       char = text[i]
#       # Encrypt uppercase characters in plain text
      
#       if (char.isupper()):
#          result += chr((ord(char) + s-65) % 26 + 65)
#       # Encrypt lowercase characters in plain text
#       else:
#          result += chr((ord(char) + s - 97) % 26 + 97)
#       return result

# text = "CEASER CIPHER DEMO"
# s = 4

# encrypt(text, s)
# print "Plain Text : " + text
# print "Shift pattern : " + str(s)
# print "Cipher: " + encrypt(text,s)

# print('hello world'.find('l')) #2 **find function**
# alien = {'color': 'green', 'points': 5}
# alien['x_position'] = 0
# #print("The alien's color is " + alien['color'])
# print(alien)

# fav_numbers = {'eric': 17, 'ever': 4}
# for number in fav_numbers.values():
#     print(str(number) + ' is a favorite')

# current_value = 1
# while current_value <= 5:
#     print(current_value)
#     current_value += 1

# def make_pizza(topping= 'bacon'):
#     """Make a single topping pizza."""
#     print("Have a " + topping + " pizza!")
# #make_pizza()
# make_pizza('pepperoni')
# def add_numbers(x, y):
#     """Add two numbers and return the sum."""
#     return x + y
# sum = add_numbers(3, 5)
# print(sum)

# class Dog():
#     """Represent a dog."""

#     def __init__(self, name):
#         """Initialize dog object."""
#         self.name = name
#     def sit(self):
#         """Simulate.sitting."""
#         print(self.name + " is sitting.")
# my_dog = Dog('Peso')

# class SARDog(Dog):
#     """Represent a search dog."""

#     def __init__(self, name):
#         """Initialize the sardog."""
#         super().__init__(name)
#     def search(self):
#         """Simulate searching."""
#         print(self.name + " is searching.")
# my_dog = SARDog('Willie')

# print(my_dog.name + " is a search dog!")
# my_dog.sit()
# my_dog.search()

# finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
# last_three = finishers[-3:]
# print(last_three)
# users[0] = 'valerie'
# users[-2] = 'ronald'
# users.insert(0, 'joe')
# users.insert(3, 'bea')
#users.sort()
#print(sorted(users))
# for user in users:
#     print("Welcome, "+ user + "!")
# num_users = len(users)
# print("We have " + str(num_users) + " users.")

# squares = [x**2 for x in range(1, 11)]
# # for x in range (1, 11):
# #     square = x**2
# #     squares.append(square)
# print(squares)

# list = [10, 20, 30, 40, 50]
# print(list.index)
# txt = "apple#banana#cherry#orange"
# x = txt.split("#", 1)
# print(x) #['Welcome', 'to', 'the', 'jungle']

filename = 'gettysburg.txt'

with open(filename) as gettysburg_file:
    lines = gettysburg_file.readlines()
# with open(filename) as gettysburg_file:
#     lines = str(gettysburg_file.read())
# print(lines)



# count the words in each list and return sum of all three:
total_words = 0
for line in lines:
    text_string = line.rstrip()
    words = line.split()
    word_count = len(words) 
    total_words += word_count
print(total_words) 

letter_count = 0
for char in text_string:
    if char.isalpha():
        letter_count += 1
print(letter_count)

#to include all outputs of a for loop into one list:
#total_words = 0
# total_words_list = []
# for line in lines:
#     #text_string = line.rstrip()
#     words = line.split()
#     word_count = len(words) 
#     #total_words += word_count
#     total_words_list.append(word_count)
# print(total_words_list)