import math
import time

def check_way(ways):
    format = []
    for way in ways:
        temp = []
        check = set(way)
        for c in check:
            count = 0
            i = 0
            while i < len(way):
                if way[i] == c:
                    count += 1
                i += 1
            s = str(c)+"("+str(count)+")"
            temp.append(s)
        format.append(temp)
    return format


def combine_2(n):
    # n = integer such as 10
    l = [i+1 for i in range(n)]
    ans = []
    for i in range(len(l)):
        for j in range(len(l)-i):
            t = (l[i],l[i+j])
            ans.append(t)

    #print(len(ans))
    return ans
    #display
    s = 0
    """
    for i in range(len(l)-1):
        j = len(l)-1-i
        #print(ans[s:s+j])
        s = s+j
    """

coin =  {
        1: 1 ,
        2 : [[2] , [1,1] ],
        5 : [[5] ,[2,2,1] ] ,
        10 : [[10] , [5,5] ] ,
        20 : [[20] , [10,10] ] ,
        50 : [[50] , [20,20,10] ] ,
        100 : [[100] , [50,50] ] ,
        200 : [[200] , [100,100] ]  }

#main seperate each coin to smaller pieces

def breakdown(number):
    # number = 5
    default = coin[number][1]
    #print(default)
    r = 0

    if len(default) % 2 != 0 :
        r = default[-1]
        #m = default
        #print(m , r)

    #start breaking
    m = default[:2] # m = [2,2]
    m = m[0] # m == 2
    #print(coin[m])
    #print(len(coin[m]))
    w = combine_2(len(coin[m]))
    #print(w)
    for way in w:
        #print(way)
        # atw stands for another way
        atw = []
        atw += coin[m][way[0]-1]
        atw += coin[m][way[1]-1]

        if r != 0:
            atw.append(r)

        atw.sort(reverse=True)
        coin[number].append(atw)


        # check if it's repetitive
        switch = True
        index = 0
        while index < len(coin[number])-1:
            if coin[number][index] == coin[number][index+1]:
                del coin[number][index]
            index += 1

"""
print(coin)
print(combine_2(2))
#print(combine_2(5))
#print(combine_2(10))
#test()
breakdown(5)
print(coin[5])
breakdown(10)
print(coin[10])
breakdown(20)
print(coin[20])
print(len(coin[20]))
#print(combine_2(6))
"""


breakdown(5)
print(len(coin[5]))
print(coin[5])
print(check_way(coin[5]))

breakdown(10)
print(len(coin[10]))
print(coin[10])
print(check_way(coin[10]))


"""
breakdown(20)
print(len(coin[20]))
print(coin[20])
x = check_way(coin[20])
for i in range(len(x)):
    print(i+1 , x[i])
"""


