import time
import math

s_normal = 0
s_advance = 0
for i in range(1000000):
    s_normal += i+1
    k = math.floor(pow(i+1,0.5))
    s_advance += k

print(s_normal, s_advance)


print(time.process_time())