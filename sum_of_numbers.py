""" 1. range + loop """

"""
sum = 0
for number in range(1,6):
    sum = sum + number


print(sum)
"""

""" 2. def """

"""
def sum_of_numbers(number):
    sum = 0
    for number in range(1, number + 1):
        sum = sum + number
    return sum


print(sum_of_numbers(28))
"""

""" 3. List Comprehension """

"""
def sum_of_numbers(number):
    return sum(number for number in range(1, number + 1))

print(sum_of_numbers(25))
"""

""" 4. Arithmetic progression """


def sum_of_numbers(number):
    return (1 + number) / 2 * number

print(sum_of_numbers(25))