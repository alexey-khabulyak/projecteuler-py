"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

i = 1
number = 600851475143
while i != number:
  i += 1
  if i == number:
    print('Result is {:.0f}'.format(number))
    break
  if not number % i:
    number = number / i
    print('Divider is {}, and result of divide is {:.0f}'.format(i, number))
    i = 1
