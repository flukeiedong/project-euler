import math, time


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
        for i in range(7, k):
            if number % i == 0:
                return False
        return True


def check_if_circular(number):
    s_number = str(number)
    r = 0
    while r < len(s_number):
        s_number += s_number[0]
        s_number = s_number[1:]
        r += 1
        if not is_prime(int(s_number)):
            return False
    return True

count = 0
for n in range(1, 1000001):
    if is_prime(n):
        if check_if_circular(n):
            count += 1
            #print(n)

print("AMOUNT =", count)
print("EXECUTED IN", time.process_time())

