import time
import math


def is_prime(number):
    if number == 1:
        return False
    if number == 2 or number == 3 or number == 5:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    if number % 5 == 0:
        return False
    else:
        k = math.ceil(pow(number, 0.5))
        for i in range(7, k+1):
            if number % i == 0:
                return False
        return True


prime_numbers = []
num = 2
while prime_numbers.__len__() != 21:
    if is_prime(num): prime_numbers.append(num)
    num += 1


print(prime_numbers[:11])
print(prime_numbers[11:])
print(sum(prime_numbers))


print("EXECUTED IN", time.process_time())

