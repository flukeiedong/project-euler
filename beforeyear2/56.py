def sum_digit(num):
    num = str(num)
    num = [int(i) for i in list(num)]
    return sum(num)

max = 0
for a in range(1, 100):
    for b in range(1, 100):
        if sum_digit(pow(a, b)) > max:
            max = sum_digit(pow(a, b))
            print("{}^{}={}".format(a, b, pow(a, b)))


print("The maximum sum is", max)

