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
