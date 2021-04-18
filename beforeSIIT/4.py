palin_check = 0
for i in range(1,1001):
    for j in range(1,1001):
        palin = i * j
        palin = str(palin)
        if palin == "".join(list(reversed(palin))):
            if int(palin) > palin_check:
                palin_check = int(palin)
                print(palin_check , i , j)