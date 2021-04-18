
def factorial(num):
    ans = 1
    for i in range(num):
        ans *= (i+1)
    return ans

limit = 100
print(sum([int(n) for n in str(factorial(limit))]))

