"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
a, b, c = 1, 2, 3
found = False
summ = 1000
while not found  or (a + b + c <= 1000):
    while c > b:
        b += 1
        c = summ - (b + a)
        if c ** 2 == a ** 2 + b ** 2:
            found = True
            print(a*b*c)
            break
    a += 1
    b = a + 1
