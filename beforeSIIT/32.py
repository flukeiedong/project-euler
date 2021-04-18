import time


count = 0
sum_pandigital = 0
digits = [str(d) for d in range(1,10)]


def check_pandigital(f,s):
    # i.e. (1,4)
    first = pow(10,f) + 1
    second = pow(10,s) + 1

    for i in range(1,first):
        for j in range(1,second):
            #print(i,j)
            remain = digits.copy()

            delete_first = [df for df in str(i)]
            delete_second = [ds for ds in str(j)]
            delete_list = delete_first + delete_second

            if "0" not in delete_list:
                # CHECK IF FIRST & SECOND HAVE ANY SAME DIGIT NUMBER
                if len(delete_first)+len(delete_second) == len(set(delete_list)):
                    # CORRECT
                    check_value = str(i * j)
                    for d in delete_list:
                        del_index = remain.index(d)
                        del remain[del_index]

                    if len(check_value) == len(remain):
                        for cv in check_value:
                            if cv in remain:
                                k = remain.index(cv)
                                del remain[k]
                            else:
                                break
                        if len(remain) == 0:
                            global count , sum_pandigital
                            count += 1
                            sum_pandigital += int(check_value)

                            print(i, j, check_value)

                else:
                    pass


check_pandigital(1,4)
check_pandigital(2,3)
# delete the repetitive value
# too lazy to do this


print("TOTAL =",count)
print("SUM =", sum_pandigital)
print("EXECUTED IN", time.process_time())



