string = input().split()[::-1]
print(string)
l = []
for x in string:
    l.append(x)
print(" ".join(l))
