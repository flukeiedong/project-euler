FILENAME = "59.txt"

f = open(FILENAME)
txt = f.readline()
t = txt.split(",")
t = [int(code) for code in t]
print(len(t), type(t), t)
s = set(t)
print(len(s), s)


t = [chr(code) for code in t]
print(len(t), type(t), t)

print(type(t[0]), type(t[1]))

# join = "".join(t)
# print(join)
# print("-----------------------------------")
# b = bytes(join, "utf-8")
# print(b.decode())




f.close()
