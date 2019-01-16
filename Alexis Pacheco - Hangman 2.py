import random
guesses = 8
playing = True

print("I am thinking of a random word what is it?")

words = ["dog", "mouse", "Volcano", "Computer!", "Concatenation", "slide", "desktop", "shoe", "sweater", "backpack"]

randword = random.choice(words)
print(random.choice)
random.choice = '*' * len(randword)
print(random.choice)

while guesses > 0:
    guess = input("Guess a letter.")
    if
