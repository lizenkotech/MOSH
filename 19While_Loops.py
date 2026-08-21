# number = 100
# while number > 0:
#     print(number)
#     number = number // 2

# number = 100
# while number > 0:
#     print(number)
#     number //= 2
"""
Python is waiting for an input
we can type something like
>>> 2 + 2 it wil evaluate it and ask for the
next input, we can ad another expression like
4
>>> 10 > 2 these steps wil continue until we press
True
>>> ^D control D
~ $
"""

Command = ""
while Command.lower() != "quit":
    Command = input(">")
    print("ECHO", Command)
