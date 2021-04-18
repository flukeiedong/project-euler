import time


def inversed(s):
    inverse = [s[len(s)-i-1] for i in range(len(s))]
    return "".join(inverse)


def is_palindrome(number):
    s_number = str(number) if type(number) is int else number
    if len(s_number) < 2: return True
    if len(s_number) % 2 != 0:
        mid = len(s_number)//2
        head = s_number[:mid]
        tail = inversed(s_number[mid+1:])
        return True if int(head) == int(tail) else False

    else:
        mid = len(s_number)//2
        head = s_number[:mid]
        tail = inversed(s_number[mid:])
        return True if int(head) == int(tail) else False


count = 0
s = 0
for n in range(1, 1000001):
    if is_palindrome(n):
        binary_n = format(n, "b")
        if is_palindrome(binary_n):
            print(n, binary_n)
            s += n
            count += 1

print(count, s)
print("EXECUTED IN", time.process_time())

