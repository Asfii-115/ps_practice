def p1(i,n):
    li = []
    for x in i:
        if i.count(x)==n:
            li.append(x)
    return list(set(li))

print(p1([1, 2, 2, 3, 1, 2, 1, 4, 3, 4, 4],2))        
