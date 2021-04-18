f = open("11","r")
data = []
for line in f:
    data.append(line.strip().split())
#print(data)
#print(len(data[1]))
def up_down():
    max = 0
    for j in range(len(data[0])):
        for i in range(len(data)-3):
            pi = 1
            for k in range(i,i+4):
                pi *= int(data[k][j])
            if max < pi:
                max = pi
                #print(pi)
                #print(i,j)
    return max

def left_right():
    max = 0
    for i in range(len(data)):
        for j in range(len(data[0])-3):
            pi = 1
            for k in range(j,j+4):
                pi *= int(data[i][k])
            if max < pi:
                max = pi
                #print(pi)
                #print(i,j)
    return max

def diagonal():
    max = 0
    for i in range(len(data)):
        for j in range(len(data[0])):

            # up right
            if i-3 < 0 or j+3 > len(data[0])-1:
                pass
            else:
                pi = 1
                for k in range(4):
                    pi *= int(data[i-k][j+k])
                if max < pi:
                    max = pi
                    #print(pi)
                    #print("UR",i,j)

            # down right
            if i+3 > len(data)-1 or j+3 > len(data[0])-1:
                pass
            else:
                pi = 1
                for k in range(4):
                    pi *= int(data[i+k][j+k])
                if max < pi:
                    max = pi
                    #print(pi)
                    #print("DR",i,j)
    return max

#print(up_down())
#print(left_right())
#print(diagonal())

check = []
check.append(up_down())
check.append(left_right())
check.append(diagonal())
print(max(check))