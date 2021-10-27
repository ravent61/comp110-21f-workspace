"""Finding duplicate letters in a word."""

<<<<<<< HEAD
__author__ = "730355583"

word: str = input("Enter a word: ")
outer_i: int = 0
is_duplicate: bool = False

while(outer_i < len(word)):
    inner_i: int = 0
    count: int = -1
    while(inner_i < len(word)):
        if word[outer_i] == word[inner_i]:
            count += 1
        inner_i += 1
    if count > 0:
        is_duplicate = True
    outer_i += 1

print("Found duplicate:", is_duplicate)
=======
__author__ = "123456789"

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
