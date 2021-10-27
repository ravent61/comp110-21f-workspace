"""Counting letters in a string."""

<<<<<<< HEAD
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
=======
__author__ = "730243388"


# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
