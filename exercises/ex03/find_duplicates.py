"""Finding duplicate letters in a word."""

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
