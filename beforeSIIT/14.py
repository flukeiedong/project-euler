limit = 1000000
sequence = []
max = 0
position = 0
'''
for num in range(1,limit+1):
    print("ROUND =",num)
    count = 0
    num_save = num
    sequence.append(num)
    while sequence[-1] != 1:
        if num % 2 == 0:
            num = num//2
            sequence.append(num)
        else:
            num = 3*num+1
            sequence.append(num)
    print(sequence)
    if max < len(sequence):
        max = len(sequence)
        position = num_save
    print("MAX =",max, "POSITION",position)
    sequence = []
'''
start = 0
for num in range(1,limit+1):
    print("Round =",num)
    count = 1
    num_save = num
    while num != 1:
        if num % 2 == 0:
            num = num//2
            count += 1
        else:
            num = 3*num+1
            count += 1
    if max < count:
        max = count
        start = num_save

print(max,start)
#MAX = 525 POSITION 837799