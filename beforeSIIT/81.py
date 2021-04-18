from time import process_time as TIME

def right(table, current):
    i, j = current # row, col
    if j >= len(table[0])-1:
        return False
    return table[i][j+1]

def bottom(table, current):
    i, j = current # row, col
    if i >= len(table)-1:
        return False
    return table[i+1][j]

def left(table, current):
    i, j = current
    if j <= 0:
        return False
    return table[i][j-1]

def up(table, current):
    i,j = current
    if i <= 0:
        return False
    return table[i-1][j]

bottom_up_path = []
def check_bottom_up(table, current, current_min_path):
    i, j = current # row, col
    if i == 0 and j == 0:
        if sum(bottom_up_path) < sum(current_min_path[:-1]):
            # print(sum(bottom_up_path), sum(current_min_path[:-1]))
            return True
        else:
            return False

    else:
        left_val = left(table, current)
        up_val = up(table, current)
        # print(left_val ,up_val)

        if not left_val:
            current = (i-1, j)
            # print(current)
        elif not up_val:
            current = (i, j-1)
            # print(current)
        else:
            if left_val < up_val:
                current = (i, j-1)
            else:
                current = (i-1, j)
            # print(current)

        i, j = current
        bottom_up_path.append(table[i][j])
        # print(bottom_up_path)
        return check_bottom_up(table, current, current_min_path)


def solve(table):
    global bottom_up_path
    min_path = []
    current_pos = (0, 0)
    count = 0
    for round in range(len(table)+len(table[0])-1):

        row, col = current_pos

        if round == 0:
            min_path.append(table[row][col])
        else:
            right_val = right(table, (row, col))
            bottom_val = bottom(table, (row, col))

            # check if pos is not exceed the table
            if not right_val:
                current_pos = (row+1, col) # use bottom position

            elif not bottom_val:
                current_pos = (row, col+1) # use right position
            #----------------------------------------

            else:
                if right_val < bottom_val:
                    current_pos = (row, col+1)
                else:
                    current_pos = (row+1, col)

            row, col = current_pos
            min_path.append(table[row][col])

            if check_bottom_up(table, current_pos, min_path):
                min_path = list(reversed(bottom_up_path.copy()))
                min_path.append(table[row][col])
                count += 1

            print("PATH", min_path)
            print("BtoU", bottom_up_path, table[row][col])
            bottom_up_path = []
    print("Times that path change >>>", count)

    return min_path



# dummy = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
# print(check_bottom_up(dummy, (2, 4), [131, 201, 96, 342, 746, 422, 111]))
# print(list(reversed(bottom_up_path)))
# path = solve(dummy)
# print(path)

f = open("81.txt", "r")

data = f.readlines()

index = 0
for d in data:
    temp = d.strip("\n")
    temp = temp.split(",")
    temp = [int(n) for n in temp]
    data[index] = temp
    index += 1

for i in data:
    if len(i) != 80:
        print(i, len(i))

path = solve(data)
print(path)
print(len(path))
print("ANS", sum(path))

print("EXECUTED IN {}s".format(TIME()))