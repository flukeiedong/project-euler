import time
import string
import math


def triangle(c):
    # ax^2 + bx + c = 0
    # a = 1 ; b = 1
    # x1,x2 = -b +- math.sqrt( pow(b,2) - 4*c ) / 2
    if 1-4*c < 0:
        return False
    else:
        x1 = (-1 + math.sqrt(1-4*c))/2
        x2 = (-1 - math.sqrt(1-4*c))/2
        if x1 == int(x1) and x1 >= 0:
            print(x1)
            return True
        if x2 == int(x2) and x2 >= 0:
            print(x2)
            return True
        return False


def read_file():
    l = []
    file = open("42.txt", "r")
    file = file.readline()
    # split the file into words
    k = 0
    while k != -1:
        prev = k+1
        k = file.find(",", k+1)
        word = file[prev:k].strip("\"")
        l.append(word)
    return l


def create_alp_table():
    alp = string.ascii_uppercase
    count = 1
    for a in alp:
        alp_value[a] = count
        count += 1


def sum_word(word):
    s = 0
    for w in word:
        s += alp_value[w]
    return s


alp_value = {}
create_alp_table()
# for k, v in alp_value.items():
#     print(k, v)


def start():
    ans = 0
    words = read_file()
    for word in words:
        c = sum_word(word)*-2
        if triangle(c):
            print(word)
            ans += 1
    print(ans)


#print(read_file())
#print(sum_word("SKY"))
start()


print("EXECUTED IN", time.process_time())


