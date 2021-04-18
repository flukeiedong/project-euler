import math

def inverse(name):
    s = ""
    for i in range(1,len(name)+1):
        s += name[-i]
    return s

def c_RD(line):
    countR = 0
    countD = 0
    for alp in line:
        if alp == "R":
            countR += 1
        elif alp == "D":
            countD += 1

        if countD > length or countR > length:
            return False
    return True


length = 7
case = []
for i in range(length*2):
    case.append(["R","D"]*pow(2,i))
print(case)
#[['R', 'D'], ['R', 'D', 'R', 'D'], ['R', 'D', 'R', 'D', 'R', 'D', 'R', 'D'], ['R', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'R', 'D', 'R', 'D']]
case = list(reversed(case))
#print(case)
route = []
temp = ""

for j in range(len(case[0])):
    for i in range(length*2):
        temp += case[i][j]
        j = math.floor(j/2)
    temp = inverse(temp)
    if c_RD(temp) :
        route.append([temp])
    temp = ""
print(route)
print(len(route))
