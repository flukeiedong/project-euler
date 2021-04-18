import math

def c_prime(num):
    if num == 1:
        return False
    elif num in [2,3,5,7]:
        return True
    elif num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    else:
        x = math.floor(pow(num,0.5))
        d = 5
        while d <= x:
            if num % d == 0:
                return False
            elif num % (d+2) == 0:
                return False
            d += 6
        return True

limit = 2000000
sum = 0
for num in range(2,limit):
    if num == 2:
        sum += num
    elif num % 2 == 0:
        pass
    else:
        if c_prime(num) == True:
            sum += num
            print(num)
        else:
            pass
print(sum)