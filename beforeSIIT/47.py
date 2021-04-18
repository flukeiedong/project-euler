# CONCEPT
# run for number in range(100000)
#   check if number is prime
# if not prime
#   begin to divide the number starting with prime[0]...
#   append it to divider[]
#   if length of set(divider) equals to 4
#       break the process


import time
import math


def divide(top, bottom):    return top / bottom


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


consecutive = []
def has_prime_factors(number):
    limit = 4
    remain = number
    composite = []
    for prime in prime_numbers:
        divisible = True
        while divisible:
            result = divide(remain, prime)
            if result.is_integer():
                composite.append(prime)
                remain = result
            else:
                divisible = False

        if remain <= 1:
            if len(set(composite)) == limit:
                consecutive.append(number)
                return True
            else:
                return False


prime_numbers = []
# first, find the prime number in range(1, 1000)
for p in range(1, 1000):
    if is_prime(p):
        prime_numbers.append(p)
# test : to find 3 consecutive numbers
for n in range(2, 1000001):
    if not is_prime(n):
        check = has_prime_factors(n)
        if check:
            if len(consecutive) == 4:
                print(consecutive)
                break
        else:
            consecutive = []
    else:
        consecutive = []


#print(has_consec_factors(340))

print("EXECUTED IN", time.process_time())


