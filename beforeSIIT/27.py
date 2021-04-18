import math
import time
start = time.time()

prime = [2,3,5,7]
def find_prime():
    for n in range(11,1001):
        k = math.floor(pow(n,0.5))
        check = True
        for p in prime:
            if p <= k:
                if n % p == 0:
                    check = False
                else:
                    pass
            else:
                break
        if check:
            prime.append(n)
find_prime()
#print(prime)

def check_prime(number):
    k = math.floor(pow(number,0.5))
    for p in prime:
        if p <= k:
            if number % p == 0:
                return False
            else:
                pass
        else:
            break
    return True
#print(check_prime(1601))

def check_consecutive(a,b):
    n = 0
    count = 0
    sum = 0
    while n >= 0:
        #pow(n,2) + a*n + b
        f = pow(n,2) + a*n + b
        if f < 0:
            return count
        if check_prime(f):
            #print(n , f)
            count += 1
            n += 1
            sum += f
        else:
            return count
#print(check_consecutive(-79,1601))

max = 0
for a in range(-1000,1001):
    for b in prime:
        ans = check_consecutive(a,b)
        if ans > max:
            max = ans
            A = a
            B = b
print(max , A , B , "product =",A*B)

end = time.time()
print("EXUCUTED IN",end-start)