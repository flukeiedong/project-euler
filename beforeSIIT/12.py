import math

def composite(num):
    #data = []
    count = 0
    if pow(num,0.5).is_integer():
        mid = pow(num,0.5)
        self = 1
    else:
        mid = math.ceil(pow(num,0.5))
        self = 0
    #print(mid)
    mid = int(mid)
    for i in range(1,mid):
        if num % i == 0:
            count += 1
            #data.append(i)
    #print(data)
    return count*2 + self

#print(composite(12753))
max = 0
num = 0
n = 1
check = composite(num)
while check <= 500:
    print("ROUND",n)
    num = (n*(n+1))//2
    print(num)
    n += 1
    check = composite(num)
    print(">>>", check)
    if max < check:
        max = check
    print("MAX =",max)
print("ANSWER",num)

