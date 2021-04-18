import time, math

pan = [str(d) for d in range(1, 8)]
clone = pan.copy()
number = []


def is_prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    else:
        k = math.ceil(pow(n, 0.5))
        for i in range(7, k):
            if n % i == 0:
                return False
        return True


def create_number(l):
    if len(l) == 2:
        num1 = "".join(number+l)
        if is_prime(int(num1)) : print(num1)
        num2 = "".join(number+list(reversed(l)))
        if is_prime(int(num2)) : print(num2)


    else:
        c = l.copy()
        for i in range(len(l)):
            #print(number)
            l = c.copy()
            jump = l.pop(i)
            number.append(jump)

            create_number(l) # l = [2, 3, 4]

            del number[-1]


create_number(pan)
print("EXECUTED IN", time.process_time())

