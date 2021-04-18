import time
start = time.time()

def sum_pow_2(n):
    sum = n*(n+1)*(2*n+1)//6
    return sum

def sum_pow_1(n):
    sum = n*(n+1)//2
    return sum

limit = 1001
print(2*(sum_pow_2(limit)-1 - 2*sum_pow_1((limit-1)//2) + (limit-1)//2)+1)

end = time.time()
print("EXECUTED IN",end-start)
