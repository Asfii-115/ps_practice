def data_reverse(data):
    d = []
    o = []
    p = 0
    for x in range((len(data) // 8)):
        d.append(data[p : p + 8])
        p += 8
    for x in d[::-1]:
        o = o + x
    return o


print(data_reverse([0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]))


def dv(data):
    d = []
    for i in range(len(data) - 8, -1, -8):
        d.extend(data[i : i + 8])
    return d


print(dv([0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]))
