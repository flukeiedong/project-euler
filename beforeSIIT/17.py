import math

write = {
    "1" : 3,#one
    "2" : 3,#two
    "3" : 5,#three
    "4" : 4,#four
    "5" : 4,#five
    "6" : 3,#six
    "7" : 5,#seven
    "8" : 5,#eight
    "9" : 4,#nine
    "10" : 3,#ten
    "11" : 6,#eleven
    "12" : 6,#twelve
    "13" : 8,#thirteen
    "14" : 8,#fourteen
    "15" : 7,#fifteen
    "16" : 7,#sixteen
    "17" : 9,#seventeen
    "18" : 8,#eighteen
    "19" : 8,#nineteen
    "20" : 6,#twenty
    "30" : 6,#thirty
    "40" : 5,#forty
    "50" : 5,#fifty
    "60" : 5,#sixty
    "70" : 7,#seventy
    "80" : 6,#eighty
    "90" : 6,#ninety
}

def onedigit(num):
    plus = write[str(num)]
    return plus

def twodigit(num):
    if num % 10 == 0:
        plus = write[str(num)]
    elif 11 <= num <= 19:
        plus = write[str(num)]
    else:
        plus = write[str(10*math.floor(num/10))]
        plus = plus + write[str(num%10)]
    return plus

def threedigit(num):
    if num % 100 == 0:
        plus = write[str(num//100)]
        plus += len("hundred")
    elif 1 <= num%100 <= 9:
        plus = write[str(math.floor(num/100))]
        plus += len("hundredand")
        plus += onedigit(num%100)
    else:
        plus = write[str(math.floor(num/100))]
        plus += len("hundredand")
        plus += twodigit(num%100)
    return plus


limit = 1000
sum = 0
for num in range(1,limit+1):
    if num <= 9:
        sum += onedigit(num)
    elif num <= 99:
        sum += twodigit(num)
    elif num <= 999:
        sum += threedigit(num)
    else:
        sum += len("onethousand")

print(sum)