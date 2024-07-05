def sumoflist(l):
    pos = 0
    count = 0
    while pos < len(l):
        count = count + l[pos]
        pos += 1
    return count

a = [8, 47, 6]
print(sumoflist(a))
