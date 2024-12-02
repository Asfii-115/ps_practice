def intersection(a, b):
    li = []
    for x in a:
        if x in b:
            li.append(x)
    return li


a = [i for i in range(0, 50000)]
b = [i for i in range(0, 50000)]

print(intersection(a, b))  # timeout O(m*n) complexity


def intersection_again(a, b):
    set_a = set(a)
    return [x for x in b if x in set_a]  # O(n+m)
