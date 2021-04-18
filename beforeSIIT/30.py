
base = [pow(x,5) for x in range(10)]
print(base)

def check(n):
    if n == 1:
        return False
    m = str(n)
    k = sum([base[int(i)] for i in m])
    if n == k:
        return True
    else:
        return False

s = 0
for num in range(1,pow(9,5)*6):
    if check(num):
        print(num)
        s += num

print("SUM =",s)

