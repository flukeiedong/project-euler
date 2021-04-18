import time


#   { 1 , 2 , 5 , 10 , 20 , 50 , 100 }
#   [ 0 , 1 , 2 ,  3 ,  4 ,  5 ,  6  ]

count = 1 # plus 200 = 200 (1 coin)
result = 200
run_loop = [ 0 , 0 , 0 , 0 , 0 , 0 , 0]
loop_val = [ 1 , 2 , 5 , 10 , 20 , 50 , 100]


def find_way(index , remain):
    global count

    if index == 0:
        mul = result - remain
        #run_loop[index] = mul
        count += 1
        print([mul] + run_loop[1:])

    else:

        q = (result-remain) // loop_val[index] # 200//100 = 2
        for mul in range(q+1):
            mul = q - mul
            run_loop[index] = mul

            if multiple_result() == result:
                count += 1
                print(run_loop)

            else:
                remain = multiple_result()
                find_way(index-1 , remain)


def check(l):
    # l == list of loop
    mul = [1,2,5,10,20,50,100]
    result = sum([l[i]*mul[i] for i in range(len(l))])
    return True



def set_to_default():
    run_loop = [ 0 , 0 , 0 , 0 , 0 , 0 , 0]


def multiple_result():
    sum_result = 0
    for i in range(7):
        sum_result += run_loop[i]*loop_val[i]

    return sum_result


find_way(6 , 0)
print(count)
print("EXECUTED IN" , time.process_time())
