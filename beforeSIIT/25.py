import time
start = time.time()

def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

x = 1
y = 1
round = 0
while 0 == 0:
    temp = x
    x = x+y
    round += 1
    if x >= pow(10,999):
        print(x)
        print(round)
        print("Fibonacci",round+2,"st")
        break
    print(round)
    y = temp

#print(Fibonacci(12))
end = time.time()
print("EXECUTED IN",end-start)