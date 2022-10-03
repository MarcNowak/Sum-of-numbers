""" 1. range + loop """

"""
sum = 0
for number in range(1,6):
    sum = sum + number


print(sum)
"""

""" 2. def """

def sum_of_numbers(number):
    sum = 0
    for number in range(1, number + 1):
        sum = sum + number
    return sum


print(sum_of_numbers(28))
