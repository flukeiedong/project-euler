import math

stop = 0

#find the 20 digit fraction
def div(num):
    t = "1"
    ans = ""
    while int(t) < num:
        ans += "0"
        t += "0"
    ans += str(int(t)//num)
    t = str(R(int(t),num))
    count = 0
    while len(str(ans)) != 1101:
        if int(t) < num:
            if count < 1:
                t += "0"
                count += 1
            else: #2nd time
                ans += "0"
                t += "0"

        else:
            ans += str(int(t)//num)
            t = str(R(int(t),num))
            global stop
            if stop == 1:
                #print(">>>",ans)
                stop = 0
                return ans[1:]
            count = 0
    return False

def R(up , down):
    r = up - (math.floor(up/down))*down
    if r == 1:
        global stop
        stop = 1
    return r

#print(div(7))
#print("0"+ str(1/7)[2:])
#print(len(div(7)))

max = 0
for i in range(2,1001):
    if div(i) != False:
        if len(div(i)) > max:
            max = len(div(i))
            temp = i

print(max)
print(temp)
print(div(temp))

