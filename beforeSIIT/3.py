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
        while d <= x :
            if num % d == 0:
                return False
            elif num % (d+2) == 0:
                return False
            d += 6
        return True

number = 600851475143
composite = []
prime = 0
for i in range(1,math.floor(pow(number,0.5))):
    if number % i == 0:
        print("DIVISION",i)
        if c_prime(i) == True:
            if prime < i:
                prime = i
                print(prime)
print("ANSWER =",prime)