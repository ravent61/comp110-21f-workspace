"""An exercise in remainders and boolean logic."""

<<<<<<< HEAD
__author__ = "730355583"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1

user_input: int = int(input("Enter an int: "))

<<<<<<< HEAD
if (user_input % 2) == 0 and (user_input % 7) == 0:
    print("TAR HEELS")
else:
    if (user_input % 2) == 0:
        print("TAR")
    else: 
        if (user_input % 7) == 0:
            print("HEELS")
        else:
            print("CAROLINA")
=======
# Begin your solution here...
num: int = int(input("Enter an int: "))

if (num % 14 == 0):
    print("TAR HEELS")
elif (num % 7 == 0):
    print("HEELS")
elif (num % 2 == 0):
    print("TAR")
else:
    print("CAROLINA")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
