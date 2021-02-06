"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730237793"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

message = randint(1,4)

if message == 1:
    print("A journey of a thousand miles begins with a single step")
else:
    if message == 2:
        print("Fortune favors the brave")
    if message == 3:
        print("Help, I'm stuck in a fortune cookie factory")
    if message == 4:
        print("Stop wishing. Start doing")





print("Now, go spread positive vibes")
