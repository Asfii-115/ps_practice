string = input().split()
l = []
for x in string:
    if len(x) % 2 == 0:
        l.append(x)
print(" ".join(l))
