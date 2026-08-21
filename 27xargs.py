# def multiply(*numbers):
#     print(numbers)
#     # return x * y


# multiply(2, 3, 4, 5)


# def multiply(*numbers):
#     for number in numbers:
#         print(number)


# multiply(2, 3, 4, 5)


# def multiply(*numbers):
#     for number in numbers:
#         total = total * number
#         total *= number


# multiply(2, 3, 4, 5)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply(2, 3, 4, 5)
