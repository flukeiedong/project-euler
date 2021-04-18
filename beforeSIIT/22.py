
def sort_alp(data):
    num = []
    for name in data:
        s = ""
        for a in name:
            add = max - len(name)
            if alp[a] < 10:
                s += "0" + str(alp[a])
            else:
                s += str(alp[a])
        s += "0" * (2 * add)
        num.append(s)
    num = sorted(num)
    #print(num)
    ans = []
    for code in num:
        code = code.rstrip("0")
        s = ""
        for i in range(0, len(code), 2):
            if code[i:i+2] == "1" or code[i:i+2] == "2":
                s += alp[int(code[i:i+2]+"0")]
            else:
                s += alp[int(code[i:i + 2])]
        ans.append(s)
    return ans

alp = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26,
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
}

f = open("22.txt","r")
names = f.readline()
data = []

k = names.find(",")
l = -1
r = 0
max = 0
while k != -1:
    data.append(names[l+1:k].strip('"'))
    if len(data[r])>max:
        max = len(data[r])
    r += 1
    l = k
    k = names.find(",",k+1)
data.append(names[l+1:].strip('"'))
if max < len(data[-1]):
    max = len(data[-1])
#print(data)
#print(data[-1])
#print(max)
#print(sort_alp(data))
final_data = sort_alp(data)

#print(final_data.index("COLIN"))

answer = 0
loc = 1
for name in final_data:
    sum = 0
    for a in name:
        sum += alp[a]
    #print(sum)
    answer += loc*sum
    #print(loc)
    loc += 1
    #print(">>>",answer)
print(answer)

f.close()