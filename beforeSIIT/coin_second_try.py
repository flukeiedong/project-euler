import time





keys = [1,2,5,10,20,50,100,200]
coin = {
    1 : [ [1,0,0,0,0,0,0] ] ,
    2 : [ [0,1,0,0,0,0,0] , [2,0,0,0,0,0,0] ] ,
    5 : [ [0,0,1,0,0,0,0] , [1,2,0,0,0,0,0] ] ,
   10 : [ [0,0,0,1,0,0,0] , [0,0,2,0,0,0,0] ] ,
   20 : [ [0,0,0,0,1,0,0] , [0,0,0,2,0,0,0] ] ,
   50 : [ [0,0,0,0,0,1,0] , [0,0,0,1,2,0,0] ] ,
  100 : [ [0,0,0,0,0,0,1] , [0,0,0,0,0,2,0] ] ,
  200 : [ ["im_a_creep."] , [0,0,0,0,0,0,2] ]
}


def combine(n):
    l = [i+1 for i in range(n)]
    ans = []
    for i in range(len(l)):
        for j in range(len(l)-i):
            t = (l[i],l[i+j])
            ans.append(t)
    return ans


def breakdown(key):
    prev_key = keys[keys.index(key)-1]
    ways = combine(len(coin[prev_key]))
    if key == 5:
        r = 1
        for way in ways:
            first_part = coin[prev_key][way[0]-1]
            second_part = coin[prev_key][way[1]-1]
            result = sum_part(first_part , second_part)
            result[0] += 1
            coin[key].append(result)
        print("Finish Breaking COIN",key)

    elif key == 50:
        print("WAITED A SEC")

    else:
        for way in ways:
            first_part = coin[prev_key][way[0]-1]
            second_part = coin[prev_key][way[1]-1]
            result = sum_part(first_part , second_part)
            coin[key].append(result)
        print("Finish Breaking COIN",key)

    #del_repetition(key)


def sum_part(first , second):
    after_sum = []
    for index in range(7):
        after_sum.append(first[index] + second[index])
    return after_sum

#def del_repetition(key):




breakdown(5)
print(coin[5])
breakdown(10)
print(len(coin[10]))
print(coin[10])

print("EXECUTED IN",time.process_time())






