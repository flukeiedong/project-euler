#common year has 365 days,besides leap year has 366

def isleap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False

months = {
    "jan" : 1,
    "feb" : 2,
    "mar" : 3,
    "apr" : 4,
    "may" : 5,
    "jun" : 6,
    "jul" : 7,
    "aug" : 8,
    "sep" : 9,
    "oct" : 10,
    "nov" : 11,
    "dec" : 12
}
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
mod = [[0,"Su"],[1,"Mo"],[2,"Tu"],[3,"We"],[4,"Th"],[5,"Fr"],[6,"Sa"]]

def find_day(start,end):
    sum = 0
    if isleap(start[2]):
        temp = 366
        if months[start[1]] > 2:
            for m in range(months[start[1]]):
                sum += days[m]
            sum += 1
        else:
            for m in range(months[start[1]]):
                sum += days[m]
    else:
        temp = 365
        for m in range(months[start[1]]):
            sum += days[m]
    sum += start[0]
    sum = temp - sum + 1

    for y in range(start[2]+1,end[2]):
        if isleap(y):
            sum += 366
        else:
            sum += 365

    if isleap(end[2]):
        if months[end[1]] > 2:
            for m in range(months[end[1]]):
                sum += days[m]
            sum += 1
        else:
            for m in range(months[end[1]]):
                sum += days[m]
    else:
        for m in range(months[end[1]]):
            sum += days[m]
    sum += end[0]
    #sum = sum - start[0] + 1
    return sum%7

x = [1,"jan",1900]
start = [1,"jan",1901]
till = [31,"dec",2000]

k = find_day(x,start)
print(k)

t = start[0]%7
for i in range(7):
    mod[k][0] = t
    k = (k+1)%7
    t = (t+1)%7
print(mod)

for n,d in mod:
    if d == "Su":
        k = n
        break
print(k)

s = 1
count = 0
for y in range(start[2],till[2]+1):
    if isleap(y):
        days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    for m in range(1,13):
        if s%7 == k:
            count += 1
            s += days[m]
        else:
            s += days[m]

print(count)
