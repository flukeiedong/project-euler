limit = 4000000
num1 = 1
num2 = 2
sum = 2
while 0 == 0:
    num1 += num2
    if num1 < limit:
        if num1 % 2 == 0:
            sum += num1
    else:
        break
    num2 += num1
    if num2 < limit:
        if num2 % 2 == 0:
            sum += num2
    else:
        break
print(sum)