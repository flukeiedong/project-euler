limit = 20
num = []
for i in range(1,limit+1):
    num += [i]
#print(num)

mul = 1
for i in range(len(num)-1):
    if num[i] != 1:
        count = 0
        for j in range(i+1,len(num)):
            if num[j] % num[i] == 0:
                num[j] = num[j]//num[i]
                count += 1
            else:
                pass
        if count != 0:
            mul *= num[i]
            num[i] = 1
        else:
            num[i] = num[i]
    else:
        pass
    print("round",i+1)
    print(num)

print(mul)
for n in num:
    mul *= n
print(mul)

