import random
guesses_left = 8
playing = True

print("I am thinking of a secret word, what is it?")

word_list = ["dog", "mouse", "Volcano", "Computer!", "Concatenation", "slide", "desktop", "shoe", "sweater", "backpack"]

wordset = set(word_list)
print(random.sample(wordset, 1))

random.sample = '*' * len()
print(random.sample)
