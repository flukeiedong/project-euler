import math, time

# consider to begin the first number with 9
# because we must multiple it with {1,2,...,n}

# test cases = { 9 , 9_ , 9__ , 9____ }


MAX = 918273645


def is_pandigital(n):
    # n is string
    digits = [str(i) for i in range(1,10)]
    n = [i for i in n]
    if "0" in n:
        return False
    else:
        if len(set(n)) == 9:
            return True
        else:
            return False



def is_mul_pandigital(n):
    global MAX
    mul = 1
    final_result = 9 # 9 digits
    result = ""
    while len(result) != final_result:
        result += str(n*mul)
        mul += 1

        if len(result) > 9:
            print("This", n, "is exceeded")
            return False

    if is_pandigital(result):
        print(n, result)
        MAX = int(result) if MAX < int(result) else MAX


for number in range(9000,9999):
    is_mul_pandigital(number)

print(MAX)
print("EXECUTED IN", time.process_time())
