def build_spiral(n):
    length = 2 * n + 1
    minus = 2 * n
    rb = length * length

    lb = rb - minus
    lt = rb - 2 * minus
    rt = rb - 3 * minus
    return [rt, lt, lb, rb]
    # frames.append([rt, lt, lb, rb])

# frame 1: length = 3, minus = 2, right-bottom = 9 = 3^2
# frame 2: length = 5, minus = 4, right-bottom = 25 = 5^2
# frame 3: length = 7, minus = 6, right-bottom = 49 = 7^2

def isprime(num):
    k = int(pow(num, 0.5)) + 1
    for d in range(2, k):
        if num % d == 0:
            return False
    return True


def check_ratio(top, bottom):
    ratio = top/bottom
    if ratio < 0.1:
        return True
    print("Ratio = %.2f" %ratio)
    return False


countPrime = 0
countDiagonal = 1

i = 1
while True:
    corners = build_spiral(i)
    countDiagonal += 4
    for c in corners:
        if isprime(c):
            countPrime += 1

    if check_ratio(countPrime, countDiagonal):
        print("At frame {} the ratio is less than 10%".format(i))
        print("Length = {}".format(2*i+1))
        break

    i += 1

