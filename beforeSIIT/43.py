import time


def is_divisable(number):
    prime = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if int(number[i+1:i+4]) % prime[i] != 0:
            return False
    return True


def create_number(l):
    if len(l) != 2:
        for i in range(len(l)):
            number.append(l[i])
            create_number(l[:i]+l[i+1:])
            del number[-1]

    else:
        way1 = l
        if is_divisable("".join(number+way1)):
            divisable_number.append(int("".join(number+way1)))
        way2 = [l[1], l[0]]
        if is_divisable("".join(number+way2)):
            divisable_number.append(int("".join(number+way2)))
        # pass to another function to check if it has the attribute


divisable_number = []
number = []
pan = [str(p) for p in range(10)]
create_number(pan)
#print(is_divisable("0146357289"))
for n in divisable_number:
    print(n)
print("SUM =", sum(divisable_number))
print("EXECUTED IN", time.process_time())

