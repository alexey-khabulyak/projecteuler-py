"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

numbers = [
    "", "one", "two", 
    "three", "four", "five", 
    "six", "seven", "eight", 
    "nine", "ten", "eleven", 
    "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", 
    "eighteen", "nineteen"
    ]
ranks = ["simple", "decades", "hundred", "thousand"]

decades = [ 
    "zero", "one",
    "twenty", "thirty", "forty", "fifty", 
    "sixty", "seventy", "eighty", "ninety"
]
def letter_word(number):
    word = ""
    length = len(str(number))
    dec = int(str(number)[-2:-1]) if length > 1 else 0
    last = int(str(number)[-1])
    i = length
    while i > 2:
        index = length - i

        #последний десяток
        if str(number)[index] != '0':
            word += "{} {} ".format(
                numbers[int((str(number)[index]))], 
                ranks[i-1]
                )
        i -= 1
    if len(word) > 0 and (dec+last) > 0:
        word += "and "
    
    if dec >= 2:
        word += "{} {}".format(decades[dec], numbers[last])

    else:
        below20index = int("{}{}".format(dec,last))
        word += "{}".format(numbers[below20index])
    return "".join(word.split())


count = 0
for i in range(1,1001):
    count += len(letter_word(i))

print (count)