import time
start = time.time()

s = [[1]]
for r in range(1,501):
    n = 1+(2*r)
    #top
    s.insert(0,[int(x) for x in range(pow(n,2)-(n-1),pow(n,2)+1)])
    #2nd
    s[1].insert(0,s[0][0]-1)
    s[1].append(s[1][n-2]+1)
    #mid
    if n == 3:
        pass
    else:
        for j in range(2,n-1):
            s[j].insert(0,s[j-1][0]-1)
            s[j].insert(n-1,s[j-1][n-1]+1)
    #base
    s.append(list(reversed([int(y) for y in range(s[n-2][n-1]+1,s[n-2][0]-1+1)])))

sum = 0
for i in range(len(s[0])):
    j = len(s[0])-1-i
    sum += s[i][i] + s[i][j]
print(sum-1) #There are "1" intercept;therefore,we must delete "1" exceeding

end = time.time()
print("EXECUTED IN",end-start)
