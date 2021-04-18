from time import process_time as TIME
import math as m


def distance(p, q):
    x1, y1 = p
    x2, y2 = q
    dis = pow(x1-x2, 2) + pow(y1-y2, 2)
    return m.sqrt(dis)


def distance_pow2(d, o=0):
    x, y = d
    dis = pow(x-o, 2) + pow(y-o, 2)
    return dis


def perpendicular(p, q):
    op = distance_pow2(p)
    oq = distance_pow2(q)
    pq = distance(p, q)
    if op + oq == pow(pq, 2):
        return True
    elif op + pow(pq, 2) == oq:
        return True
    elif oq + pow(pq, 2) == op:
        return True
    return False


n = 2
c = 0
for p_x in range(n+1):
    for p_y in range(n+1):
        for q_x in range(n+1):
            for q_y in range(n+1):
                if perpendicular((p_x, p_y), (q_x, q_y)):
                    c += 1
                    print(p_x, p_y, q_x, q_y)

print(c)
print("EXECUTED IN {}s".format(TIME()))