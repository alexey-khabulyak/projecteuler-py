"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

smallest = 0
max_value = 20
found = False
while not found:
    smallest += max_value
    for i in range(1,max_value + 1):
        if smallest % i:
            break
        if i == max_value:
            found = True
print (smallest)