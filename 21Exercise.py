count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")


"""Exercise 1 — Print numbers

Write a for loop that prints:

1
2
3
4
5

Hint: Use range()."""

"""🟢 Exercise 2 — Even numbers

Write a program that prints all the even numbers from 1 to 10.

Expected output:

2
4
6
8
10

Hint: You already know how to do this! 😉"""

"""Exercise 3 — Odd numbers

Now do the opposite.

Print all the odd numbers from 1 to 10.

Expected output:

1
3
5
7
9

💡 Hint: Think about what the remainder
is when an odd number is divided by 2."""

"""Exercise 4 — Count the even numbers

Write a program that:

Goes through numbers 1 to 10.
Prints every even number.
At the end says:
There are 5 even numbers

Expected output:

2
4
6
8
10
There are 5 even numbers

💡 Hint: You'll need a count variable."""

"""Exercise 5 — Bigger range

Print all the even numbers between 1 and 20.

Expected output:

2
4
6
8
10
12
14
16
18
20

Then make Python count them and print:

There are 10 even numbers"""

"""Exercise 6 — Don't print 6

Print the even numbers from 1 to 10, but stop completely when you reach 6.

Expected output:

2
4

💡 This is where you should use:

break

Think about what we just learned:

break = 🛑 STOP THE LOOP."""

"""What will this code output?

count = 0

for number in range(1, 6):
    if number % 2 == 0:
        print(number)
        count = count + 1

print(count)

Don't run it. Try to work it out yourself.

Write down what happens with:

1 → ?
2 → ?
3 → ?
4 → ?
5 → ?

Then tell me your answers,
and I'll check them one by one with you. 😊"""
