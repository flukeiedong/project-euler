
number = set()
for a in range(2,101):
    for b in range(2,101):
        temp = pow(a,b)
        number.update([temp])
#print(number)
print(len(number))
