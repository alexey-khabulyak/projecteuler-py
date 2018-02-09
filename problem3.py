"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from random import choice
n = 13195
# первый возможный делитель. Т.к. надо найти наибольший то идём вниз
# round округляет до чётного. нам нужны не чётные.
delimiter = round(n / 2) + 3
while delimiter > 1:
    delimiter -= 2
    # проверяем делится ли без остатка
    if (n / delimiter) % 1 == 0.0:
        continue
    print ("Delimiter found: {}, Ferma checking".format(delimiter))
    # малая теорема Ферма:
    a = choice(range(2, delimiter))
    if (a ^ delimiter) % delimiter == a % delimiter:
        print ("Ferma: {}".format(delimiter) )
    
print (delimiter)

