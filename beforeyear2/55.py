def reverse_number(num):
    num = str(num)
    reverse_num = num[len(num)-1::-1]
    return int(reverse_num)


def checkifpalindrome(num):
    if num == reverse_number(num):
        return True
    return False


def iteration_process(num):
    result = 0
    print()
    print(num)
    print()
    for r in range(50):
        if result == 0:
            print("ROUND:{} of {}".format(r + 1, num))
            result = num + reverse_number(num)
            print("{} + {} = {}".format(num, reverse_number(num), result))
        else:
            print("ROUND:{} of {}".format(r + 1, result))
            temp = result
            result = result + reverse_number(result)
            print("{} + {} = {}".format(temp, reverse_number(temp), result))

        if checkifpalindrome(result):
            return True
    return False


SCOPE = 10000
count = 0
for num in range(10, SCOPE):
    if iteration_process(num):
        # print(num)
        pass
    else:
        print("{} is Lychrel number".format(num))
        count += 1

print("Count Lychrel number:", count)

