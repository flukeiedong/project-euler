
def c_prime(number):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
            #print(count)
            if count > 2:
                return False
    return True

limit = 10001
prime = []
x = 2
r = 0
while len(prime) != limit:
    if c_prime(x) == True:
        prime.append(x)
        r += 1
        print(prime[-1], r)
    x += 1
#print(prime)