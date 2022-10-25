#ROT Cipher


rot13={
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m",
}

user_word = ""

user = input("Enter a word: ")

for char in user:
   user_word += rot13[char]
print(user_word)
  
 





