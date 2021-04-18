import time

s = ""
counter = 0
while len(s) <= 1000001:
    s += str(counter)
    counter += 1
    #print(counter, len(s))

print(s[10], s[100], s[1000], s[10000], s[100000], s[1000000])
mul = [s[10], s[100], s[1000], s[10000], s[100000], s[1000000]]
ans = 1
for m in mul:
    ans *= int(m)
print("RESULT =", ans)

print("EXECUTED IN", time.process_time())

