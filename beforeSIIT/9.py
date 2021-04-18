limit = 1000

for c in range(1,limit):
    for b in range(1,limit-c):
        a = limit-b-c
        if a > 0 and a < c and b < c:
            #print(a,b,c)
            #print(a+b+c)
            if pow(a,2) + pow(b,2) == pow(c,2):
                print(a*b*c)
                print(">>>",(a,b,c))
        else:
            pass


