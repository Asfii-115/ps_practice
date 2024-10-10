def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 == 1:
            return x


print(find_it([0, 1]))
