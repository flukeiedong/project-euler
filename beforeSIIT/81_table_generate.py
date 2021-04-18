import random as rd

x = 5; y =5

for i in range(5):
    for j in range(5):
        print(rd.randint(1, 1000), end="\t")
    print()
