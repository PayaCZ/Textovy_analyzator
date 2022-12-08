"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavel Šmíd
email: 78.78@seznam.cz
discord: Pavel Šmíd#2969

"""
from task_template import TEXTS

from username_password import users


print('-' * 57)    

name = input("username: ")
pass_word = input("password: ")

if users.get(name) == pass_word:
    print("the name and password is fine")
else:
    print("unregistered user, terminating the program..")
    quit()

print('-' * 57)    

print("Welcome to the app", name+"\n"+"We have 3 texts to be analyzed.")    

print('-' * 57)    


text_selection  = input("Enter a number btw. 1 and 3 to select: ")

if text_selection is "1":
    text = TEXTS[0]
elif text_selection is "2":
    text = TEXTS[1]
elif text_selection is "3":
    text = TEXTS[2]
else:
    print('-' * 57)    
    print("You entered the wrong number or letter, terminating the program.....")    
    print('-' * 57)    
    
    quit()
    
print('-' * 57)    

print(f"{text:0}\n")

print('-' * 57)    

text_large = []
text_small = []
text_first_capital = []
text_number = []

clean_words = list()

for word in text.split():
    clean_words.append(word.strip(",.:;"))

for i in clean_words:
    if i.isupper():
        text_large.append(True) 
    elif i.islower():
        text_small.append(True)
    elif i[0].isupper():    
        text_first_capital.append(True)
    elif  i.isnumeric():
        text_number.append(True)

num = [int(num) for num in clean_words if num.isdigit()]      
num = sum(num)

print("There are", len(clean_words), "words in the selected text.")
print("There are",text_first_capital.count(True) , "titlecase words.")
print("There are",text_large.count(True) , "uppercase words.")
print("There are",text_small.count(True) , "lowercase words.")
print("There are", text_number.count(True), "numeric strings.")  
print("The sum of all the numbers", num   )
print()  
print(f"{'-' * 40}\nLEN|{'OCCURENCES':>15}{'|NR.':>10}\n{'-' * 40}")

word_count: dict = dict()

for word in clean_words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] = word_count[word] + 1

for key, value in sorted(word_count.items()):
    print(f"{len(key):3}|{'*' * len(key):>13} {'|':>8}{value:>1}")


    
    
    
    
    
    