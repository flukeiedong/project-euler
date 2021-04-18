def calculate(a, b):
    # a,b -> fraction of a/b
    top = b
    bottom = 2*b+a

    # ------------------- DISPLAY PART -----------------------
    # print("___1___")
    # print("2 + {}/{}   =   {}/{}".format(a, b, top, bottom))
    # print("Result = {}/{}".format(top+bottom, bottom))
    # ---------------------------------------------------------

    return top, bottom

count = 0
top, bottom = 1, 2
for i in range(999):
    print("\nROUND", i+1, "\n")
    top, bottom = calculate(top, bottom)
    if len(str(top+bottom)) > len(str(bottom)):
        print("Result = {}/{}".format(top + bottom, bottom))
        count += 1
        print("Counting.....")

print("Count =", count)

