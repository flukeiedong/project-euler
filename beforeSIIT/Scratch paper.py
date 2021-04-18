import time


def factorial(n):
    value = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1,n+1):
            value *= i
        return value


fac_table = [factorial(d) for d in range(10)]


def sum_fac(num):
    s = 0
    str_num = str(num)
    for n in str_num:
        s += fac_table[int(n)]
    return s


def start():
    for num in range(1, 1000000):
        if num == sum_fac(num):
            print(num)


start()
print(fac_table)
#print(sum_fac(1999))

print("EXECUTED IN", time.process_time())

