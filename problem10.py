"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

"НЕ ОЧЕНЬ ХОРОШЕЕ РЕШЕНИЕ. НАДО БУДЕТ ПЕРЕДЕЛАТЬ"

def is_prime(num):
    if num == 1:
        return False
    # двойка простое число
    if num == 3:
        return True
    for i in range(3, round(num/2) + 1, 2):
        if not num % i:
            return False
    return True


number = 1
summ = 2 # 2 will be skipped
while number < 2000000:
    if is_prime(number):
        summ += number
    number += 2
print (summ)