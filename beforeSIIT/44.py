import time, math


def pn(n): return n*(3*n-1)


def plus(A, B): return pn(A)+pn(B)


def minus(A, B): return pn(B)-pn(A)


def in_root(C): return 1+12*C


def different(A, B): return (pn(B)-pn(A))/2


diff_min = 1000000000
count = 0
for a in range(1, 3001):
    for b in range(a+1, 3001):
        # c1 = plus(a, b)
        ir_c1 = math.sqrt(in_root(plus(a, b)))
        if ir_c1.is_integer():
            # check +1 then % 6
            if (ir_c1+1) % 6 == 0:
                # check for minus
                ir_c2 = math.sqrt(in_root(minus(a, b)))
                if ir_c2.is_integer():
                    if (ir_c2+1) % 6 == 0:
                        print(a, b)
                        diff = different(a, b)
                        count += 1
                        if diff < diff_min : diff_min = diff


        # send a & b to function plus and minus


print(count)
print("MIN =", diff_min)
print("EXECUTED IN", time.process_time())


