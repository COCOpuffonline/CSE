import random
word = ["dog", "mouse", "Volcano", "Computer!", "Concatenation", "slide", "desktop", "shoe", "sweater", "backpack"]
random_word = random.choice(word)
random.choice = '*' * len(word)
print(random_word)