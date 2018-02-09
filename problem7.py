found = False
counter = 1 # 2 will be skipped
number = 1
while counter < 10001:
    number += 2
    for i in range (2, number):
        if not number % i:
            # нет остатка. значит не простое
            break
        # последняя итерации. значит число простое
        if i == number - 1:
            counter += 1
print (number)