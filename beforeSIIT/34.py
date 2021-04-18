import time

sum_fac = 0
number = ""


def factorial(n):
    value = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1,n+1):
            value *= i
        return value


def put_number(n, *code):
    global number
    check = []
    for c in code:
        check.append(c)

    if len(check) == 0:
        if len(number) != 0:
            number += n
        else:
            number = n
    else:
        number += n
        temp = number
        number = number[:-1]
        return int(temp)


def find_index(k):
    if k == 2:
        return 5
    elif k == 3:
        return 6
    elif k == 4:
        return 7
    elif k == 5:
        return 8
    else:
        return 9


def each_digit(numbers, k):
    global sum_fac, number
    if k == 1:
        for l in numbers:
            sum_fac += fac_val[int(l)]
            check_val = put_number(l, "EXECUTE")

            if check_val == sum_fac:
                print("RESULT =", sum_fac)
            else:
                print("!=", check_val)

            sum_fac -= fac_val[int(l)]
    else:
        for i in numbers:
            sum_fac += fac_val[int(i)]
            put_number(i)
            each_digit(numbers, k-1)
            sum_fac = 0
            number = ""


def digit_factorial(k):
    # k is the number of digits
    index = find_index(k)
    numbers = digits[:index]

    # Begin recursive function

    each_digit(numbers, k)

    # for i in numbers:
    #     for j in numbers:
    #         print(i, j, factorial(int(i))+factorial(int(j)))
    #         if int(i+j) == factorial(int(i))+factorial(int(j)):
    #             print(int(i+j))
    #         else:
    #             print("NOPE", int(i+j))


digits = [str(dg) for dg in range(10)]
fac_val = [factorial(n) for n in range(10)]

digit_factorial(2)
digit_factorial(3)


print("EXECUTED IN", time.process_time())



