"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
f1 = f2 = 999
maximum = result = 0
while f2 > 0:
    f1 = f2
    while str(f1 * f2) != str(f1 * f2)[::-1]:
        f1 -= 1
    else:
        result = f1 * f2
        maximum = result if maximum < result else maximum
    f2 -= 1
print (maximum)
