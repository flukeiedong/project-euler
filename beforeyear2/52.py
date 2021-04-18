def check_digit(a, b):
    a = str(a)
    b = str(b)
    for d in a:
        if d in b:
            index = b.index(d)
            b = b[:index] + b[index+1:]
        else:
            return False
    return True


def check_digits(x):
    for i in range(2, 7):
        if check_digit(x, x*i):
            print(i, x, x*i)
            # pass
        else:
            return False
    return True



def len_str(x):
    return len(str(x))


def check_len(x):
    length = len_str(x)
    for i in range(1, 7):
        if length != len_str(x*i):
            # print(x)
            return False
    # print(x)
    global count
    count += 1
    return True


def permutedMultiple(x):
    if check_len(x):
        if check_digits(x):
            return True

count = 0
SCOPE_X = 1000000
for x in range(1, SCOPE_X):
    if permutedMultiple(x):
        print("ANS", x)

print("Count same length of digits {} from {}".format(count, SCOPE_X))
