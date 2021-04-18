import math

def d(num):
    if num == 1:
        data.append(0)
        return 0
    sum = 0
    for i in range(1,math.ceil(pow(num,0.5))):
        if num % i == 0:
            sum += i
            sum += num//i
        else:
            pass
    data.append(sum-num)
    return sum-num

data = []
pos = []
#print(d(220))
#print(d(284))

limit = 10000
for i in range(1,limit+1):
    d(i)
    pos.append(i)
print(data)
print(pos)
sum = 0
for i in range(1,limit):
    x = data[i]
    if i+1 == x:
        pass
    else:

        if x-1 < limit-1:
            if i+1 == data[x-1]:
                print(i+1 , x)
                sum += i+1
            else:
                pass
        else:
            if d(x) == i+1:
                print(i+1 , x)
                sum += x
            else:
                pass

print(sum)

