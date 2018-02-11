"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def next_number(number):
    # не чётное
    if number % 2:
        return (3 * number + 1)
    else:
        return number / 2
max_value = 0
for i in range(1000001):
    number = i
    count = 1
    while number > 1:
        number = next_number(number)
        count += 1
    
    if max_value < count:
        max_value = count
        print ("{}:{}".format(i, max_value))
