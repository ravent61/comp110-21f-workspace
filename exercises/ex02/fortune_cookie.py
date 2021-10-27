"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730243388"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
<<<<<<< HEAD
print("Your fortune cookie says...")
random: int = randint(1, 4)
fortune: str
if random == 1:
    fortune = "You will meet your husband"
else: 
    if random == 2:
        fortune = "You will find a $5 bill"
    else:
        if random == 3:
            fortune = "You will have 3 kids"
        else:
            fortune = "absolutely nothing"

print(fortune)
print("Now, go spread positive vibes!")
=======

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
print("Now, go spread positive vibes!")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
