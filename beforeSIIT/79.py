# FILE
def import_file():
    f = open("79.txt", "r")
    # print(f.readlines())
    for l in f.readlines():
        temp = l.rstrip("\n")
        add_order(temp)
        data.append(temp)
    f.close()


def create_order():
    for i in range(10):
        order[str(i)] = []


def add_order(num):
    # check first pos
    for i in [1, 2]:
        if num[i] not in order[num[0]]:
            order[num[0]].append(num[i])
    # check second pos
    if num[2] not in order[num[1]]:
        order[num[1]].append(num[2])


def indentify_pair(pc):
    for i in range(len(pc)):
        for j in range(i+1, len(pc)):
            if pc[i] == pc[j]:
                return i, j
    return False


def add_passcode(num):
    global passcode
    print(num, passcode)
    for n in num:
        print(n)
        if n in passcode:
            index = passcode.index(n)
            passcode = passcode[:index] + num + passcode[index+1:]

        else:

            passcode += num


def delete_pair(i, j):
    for index in range(i+1, j):
        for o in order[index]:
            if o == passcode[i]:
                del passcode[i]
                return
    del passcode[j]


def check_passcode():
    if indentify_pair(passcode):
        i, j = indentify_pair(passcode) # i, j -> index of pair
        delete_pair(i, j)
        check_passcode()




data = []
order = dict1
create_order()
import_file()
print(data)
# print order
for k, v in order.items():
    print(k, v)

passcode = data[0]
# solve()
for i in range(1, 10):
    # send 3 digit attempt
    add_passcode(data[i])
    check_passcode()
