import math

limit = 28123

def compose(number):
    if number == 1:
        return 1
    sum = 0
    if float(number**0.5).is_integer():
        sum += int(number**0.5)
    k = math.ceil(number**0.5)
    for n in range(2,k):
        if number % n == 0:
            sum += n
            sum += number//n
    return sum+1

abd = list()

def create_abundant():
   for num in range(1,limit):
       if compose(num) > num:
           abd.append(num)

create_abundant()
print(abd)

data = []
for i in range(len(abd)):
    for j in range(i,len(abd)):
        num = abd[i] + abd[j]
        if num <= limit:
            data.append(num)
data = set(data)
print(limit*(limit+1)/2 - sum([n for n in data]))

