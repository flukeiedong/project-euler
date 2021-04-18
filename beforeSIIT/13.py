f = open("13","r")
sum = 0
for line in f:
    line = line.strip()
    sum += int(line)
print(sum)
sum = str(sum)
print(sum[0:10])
f.close()