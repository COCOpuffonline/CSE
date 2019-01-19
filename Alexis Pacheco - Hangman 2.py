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
<<<<<<< HEAD
<<<<<<< HEAD
=======
print(word_selection)
>>>>>>> d3174b2d5978b7fb251d2beae40197a895851db6
=======
print(word_selection)
>>>>>>> d3174b2d5978b7fb251d2beae40197a895851db6

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter -")
    print('\n' * 10)
    if user_guess in word_selection:
        print("You got it right!")
        for i in range(len(word_selection)):
            if user_guess in word_list:
<<<<<<< HEAD
<<<<<<< HEAD
                            word_list.pop(i)
=======
                word_list.pop(i)
>>>>>>> d3174b2d5978b7fb251d2beae40197a895851db6
=======
                word_list.pop(i)
>>>>>>> d3174b2d5978b7fb251d2beae40197a895851db6
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
<<<<<<< HEAD
<<<<<<< HEAD
        print("The word was (%s)" % word_selection)
=======
>>>>>>> d3174b2d5978b7fb251d2beae40197a895851db6
=======
>>>>>>> d3174b2d5978b7fb251d2beae40197a895851db6
    if len(word_list) == 0:
        print("You won!")
        print("The word was %s" % word_selection)

