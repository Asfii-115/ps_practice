string = input().split()
l = []
for x in string:
    c = x.capitalize()
    l.append(c)

print(l)
s = []
for x in l:
    leng = len(x)
    n = x[leng - 1].upper()
    f = x[: leng - 1] + n
    s.append(f)

print(s)

# s = "welcome to geeksforgeeks"
# print("String before:", s)
# a = s.split()
# res = []
# for i in a:
#     x = i[0].upper()+i[1:-1]+i[-1].upper()
#     res.append(x)
# res = " ".join(res)
# print("String after:", res)
