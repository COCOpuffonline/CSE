import random
import string
words = ["dog", "mouse", "Volcano", "Computer!", "Concatenation", "slide", "desktop", "shoe", "sweater", "backpack"]
guesses = 8
output = []

list_of_letters = string.ascii_letters

word_selection = random.choice(words)
word_list = list(word_selection)
length = len(word_selection)

for i in range(length):
    output.append("* ")
print("".join(output))
print(word_selection)

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter -")
    print('\n' * 10)
    if user_guess in word_selection:
        print("You got it right!")
        for i in range(len(word_selection)):
            if user_guess in word_list:
                word_list.pop(i)
        for i in range(len(word_selection)):
            if word_selection[i] == user_guess:
                output.pop(i)
                output.insert(i, user_guess)
        print("".join(output))
    else:
        print("You got it wrong!")
        guesses = (guesses - 1)
        print(guesses)
    if guesses <= 0:
        print("You ran out of guesses. GAME OVER")
    if len(word_list) == 0:
        print("You won!")
        print("The word was %s" % word_selection)

