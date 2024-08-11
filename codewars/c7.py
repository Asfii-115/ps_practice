def count_by(x, n):
    li = []
    for i in range(1, n + 1):
        li.append(x * i)
    return li


print(count_by(2, 5))
