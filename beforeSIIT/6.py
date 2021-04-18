limit = 100
sum1 = 0
sum2 = 0
for i in range(1,limit+1):
    sum1 += pow(i,2)
for j in range(1,limit+1):
    sum2 += j
sum2 = pow(sum2,2)
print(sum1,sum2)
print(sum2 - sum1)