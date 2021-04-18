import math
limit = 1000
sum = 0
for i in range(1,math.ceil(limit/3)):
    sum += i*3
for j in range(1,math.ceil(limit/5)):
    sum += j*5
for k in range(1,math.ceil(limit/15)):
    sum -= k*15
print(sum)