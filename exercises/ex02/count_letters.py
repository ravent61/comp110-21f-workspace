"""Counting letters in a string."""

from random import randint
__author__ = "730355583"


# Begin your solution here...
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