def merge(w1, w2):
    w3 = ""
    x = 0
    while x < len(w1) or x < len(w2):
        if x < len(w1):
            w3 += w1[x]
        if x < len(w2):
            w3 += w2[x]
        x += 1
    return w3


print(merge("abcd", "pqr"))
