import time


sqr_val = [pow(d, 2) for d in range(1000)]
print("FINISH TABLE")
def is_right_triangle(a, b, c):
    if sqr_val[c] == sqr_val[a]+sqr_val[b]:
        return True
    return False


count = 0
test = []
def count_triangle(p):
    global count
    for a in range(1, p//3+1):
        for b in range(a, p//2+1):
            c = p - a - b
            if a + b > c > b and c > a:
                #print(a, b, c)
                if is_right_triangle(a, b, c):
                    #test.append((a, b, c))
                    count += 1
    temp_count = count
    count = 0
    return temp_count


def start():
    result = []
    for p in range(1, 1001):
        c = count_triangle(p)
        result.append(c)
    print(result)
    print("MAX =", max(result))
    print(result.index(max(result)))


start()
# print(count_triangle(840), test)

print("EXECUTED IN", time.process_time())






