import random

print("I am thinking of a random word what is it?")

words = ["dog", "mouse", "Volcano", "Computer!", "Concatenation", "slide", "desktop", "shoe", "sweater", "backpack"]

randword = random.choice(words)
print(random.choice(words))

random.choice = '*' * len(randword)
print(random.choice)
