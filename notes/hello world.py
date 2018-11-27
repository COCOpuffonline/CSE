"""
print("Hello World!")

# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple blank lines here.")

# Math
print(3 + 5)
print(5 - 2)
print(3 * 5)
print(6 / 2)

print("Figure this out...")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one...")
print(6 % 2)
print(5 % 2)
print(11 % 4)   # Modulus (Remainder)

# Powers
# What is 2^20
print(2 ** 100)

# Talking input
name = input("What is your name?")
print("Hello %s." % name)

age = input("How old are you? > _")
print("%s!? You belong in a museum." % age)
print()
print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name = "Alexis Mobile"
car_type = "Tesla"
car_cylinders = 16
car_miles_per_gallon = 0.01

# Make it print "I have a car called Alexis Mobile. It is a Tesla."
print("I have a car called %s. It is a %s" % (car_name, car_type))

# Recasting
real_age = int(input("How old are you again"))
hidden_age = real_age + 5
print("This is your real age: %d" % hidden_age)
"""

"""
This is a multi-line comment
Anything between the "s is not run.
"""


# Functions
def say_it():
    print("Hello World!")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2*x +3)


f(1)
f(5)
f(5000)


# Distance Formula
def distance (x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# Loops
for i in range(10000):  # This give the numbers 0 through 4
    say_it()

for i in range(10):
    print(i+1)

for i in range(5):
    f(i)

# While loops
a = 1
while a < 10:
    print(a)
    a += 2   # This is the same as saying a = a + 1


"""
At the moment you START the loop:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""

# Control Structures (If statement)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

# "Random" Notes
import random   # This should be on line 1
print(random.randint(0, 100))


# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3  # A is set to 3
a == 3 # Is a equal to 3?
"""

# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black", "red", "grey", "purple", "brown", "silver"]
# USE SQUARE BRACKETS!!!!!
print(colors[1])
print(colors[0])

# Length of the list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "Green"
print(colors)

# Looping through lists
for item in colors:
    print(item)

'''
1. Make a list with 7 items
2. Change the 3rd thing in the list
3. Print the item
4. Print the full list
'''

new_list = ["Lenovo", "Hp", "MSI", "Razer", "Alienware", "Asus", "Acer"]
new_list[2] = "MacBook"
print(new_list)
print("The last thing in the list is %s" % new_list[len(new_list) - 1])

# Slicing a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:4])


food_list = ["pizza", "tacos", "flan", "ceviche", "enchiladas", "sushi", "spaghetti", "hot wings", "chicken", "pozole",
             "salmon", "lobster", "noodles", "tamales", "pie", "chili", "sandwich", "soup", "burrito", "chips",
             "carne asada", "cake", "salad"]
print(len(food_list))

# Adding stuff to a list
food_list.append("bacon")
food_list.append("eggs")
# Notice that everything is object.method (parameters)
print(food_list)

food_list.insert(1, "eggo waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)

"""
1. make a new list with 3 items
2. add a 4th item to the list
3. remove one of the first three items from the list
"""

gpu_list = ["gtx 1070", "gtx 1050", "gtx 1050 ti"]
print(gpu_list)

gpu_list.append("rtx 2080")
print(gpu_list)

gpu_list.remove("gtx 1070")
print(gpu_list)

# Tuples
brands = ("apple", "samsung", "HTC")  # Notice the parentheses

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Turn a list in a string
print("".join(list1))

for i in range(len(list1)):  # i goes through all indices
    if list1[i] == "u":  # if we find a U
        list1.pop(i)  # remove the i-th index
        list1.insert(i, "*")  # Put a * there instead

'''
for character in list1:
    if character == "u":
        # replace with a *
        current_index = list1.index)characters)
        list1.pop(current_index
        list1.insert(current _index, "*")
'''

# Turn a list into a string
