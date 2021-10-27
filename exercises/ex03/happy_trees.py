"""Drawing forests in a loop."""

__author__ = "730355583"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
<<<<<<< HEAD
outer_i: int = 1
if (depth <= 0) is False:
    while(outer_i < depth + 1):
        inner_i: int = 0
        treees: str = ""
        while(inner_i < outer_i):
            treees += TREE
            inner_i += 1
        print(treees)
        outer_i += 1
=======

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
