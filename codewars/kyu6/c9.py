def order(sentence):
    # code here
    li = []
    s = sentence.split()
    for i in range(1, 10):
        for item in s:
            if str(i) in item:
                li.append(item)

    return li


print(order("is2 Thi1s T4est 3a"))
