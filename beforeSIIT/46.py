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


def is_goldbach(prime, number):
    # number - prime == 2 * S.thing^2
    check = math.sqrt((number-prime)/2)
    return True if check.is_integer() else False


def check_if_goldbach(number):
    rev_prime_numbers = list(reversed(prime_numbers))
    for p in rev_prime_numbers[1:]:
        if is_goldbach(p, number):
            # print(number, p)
            return
    goldbach_suck.append(number)


goldbach_suck = []
prime_numbers = []
for n in range(3, 100000):
    if len(goldbach_suck) > 0: break
    if is_prime(n):
        prime_numbers.append(n)

        if n > 5:
            odd_number = prime_numbers[-2]+2
            while odd_number != prime_numbers[-1]:
                # check if the number is Goldbach or not ?
                # for loop all the current prime_numbers

                check_if_goldbach(odd_number)
                odd_number += 2


print(prime_numbers)
print(goldbach_suck)

print("EXECUTED IN", time.process_time())


