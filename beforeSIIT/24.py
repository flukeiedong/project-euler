r = 0
def permute(s):
    if len(s) == 2:
        for i in range(2):
            s[0],s[i] = s[i],s[0]
            global r
            r += 1
            print(r,"".join(b+s))
            if r == 1000000:
                exit()


    else:
        temp = s.copy()
        for i in range(len(s)):
            s = temp.copy()
            b.append(s.pop(i))
            permute(s)
            del b[-1]

b = []
word = "0123456789"
l = len(word)
word = list(word)
clone = word.copy()
permute(word)
