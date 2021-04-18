import time, math


def triangle_val(n): return n*(n+1)/2


def discriminant(a, c): return 1-4*a*c


def is_pentagon(value):
    c = -2 * value
    n = (1+math.sqrt(discriminant(3, c)))/6 # only consider on positive value
    return True if n.is_integer() else False


def is_hexagon(value):
    c = -1 * value
    n = (1+math.sqrt(discriminant(2, c)))/4
    return True if n.is_integer() else False


# start n at 286
n = 286
found = False
while not found:
    val = triangle_val(n)
    if is_pentagon(val) and is_hexagon(val):
        print(n, val)
        found = True
    n += 1


print("EXECUTED IN", time.process_time())


