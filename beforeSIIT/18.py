heigth = 100
tri = []
for i in range(0,heigth):
    line = input().split()
    tri += [line]
#print(tri)
tri = list(reversed(tri))
#print(tri)
for i in range(len(tri)):
    for j in range(len(tri[i])):
        tri[i][j] = int(tri[i][j])
print(tri)

plus = []
for line in tri:
    if len(plus) > 0:
        for x in range(len(plus)):
            line[x] += plus[x]
    else:
        pass
    plus = []
    for i in range(len(line)-1):
        plus.append(max(line[i],line[i+1]))
    print(plus)
print(tri[-1])