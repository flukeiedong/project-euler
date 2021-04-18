import time


# top "numerator" < 100
# bottom "denominator" < 100
numerator = 100
denominator = 100
lowest_denominator = 1


def check_if_trivial(top, bottom):
    temp = str(top) + "/" + str(bottom)
    fraction_value = top/bottom
    if int(fraction_value) < 1:
        top = [n for n in str(top)]
        bottom = [d for d in str(bottom)]
        if has_something_in_common(top, bottom):
            #print(top, bottom)
            if top[0] in bottom:
                index = bottom.index(top[0])
                del top[0], bottom[index]
            else:
                index = bottom.index(top[1])
                del top[1], bottom[index]

            if int(bottom[0]) != 0 and int(top[0])/int(bottom[0]) == fraction_value:
                print(temp, top[0], bottom[0], fraction_value)
                global lowest_denominator
                parts = temp.split("/")
                lowest_denominator = lowest_denominator * int(parts[1]) / int(parts[0])


def has_something_in_common(top, bottom):
    #print(len(top) , len(bottom) , len(set(top+bottom)))
    if len(set(top))+len(set(bottom)) == len(set(top+bottom)):
        return False
    else:
        return True


for t in range(10, numerator):
    for b in range(10, denominator):
        if t % 10 == 0 and b % 10 == 0:
            pass
        else:
            check_if_trivial(t, b)

print("ANSWER =", int(lowest_denominator))
print("EXECUTED IN", time.process_time())



