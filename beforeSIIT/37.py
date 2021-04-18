import math, time


def is_prime(number):
    if number == 1 or number == 0:
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


def is_truncatable(number):
    s_number = str(number)
    r = 1
    while r < len(s_number):
        # from right to left
        s_number_rtl = s_number[r:]
        if not is_prime(int(s_number_rtl)):
            return False

        # from left to right
        s_number_ltr = s_number[:len(s_number)-r]
        if not is_prime(int(s_number_ltr)):
            return False
        print(s_number_rtl, s_number_ltr)
        r += 1

    return True


#print(is_truncatable(1001))


count = 0
number = 8
ans = []
while count < 11:
    if is_prime(number):
        if is_truncatable(number):
            ans.append(number)
            count += 1
    number += 1
    print(number)

print(ans)
print(sum(ans))
print("EXECUTED IN", time.process_time())
