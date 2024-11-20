def parts_sums(ls):
    i = 0
    lst = []
    while i <= len(ls):
        lst.append(sum(ls[i:]))
        i += 1

    return lst


print(parts_sums([0, 1, 3, 6, 10]))

# full sum niye then oita theke ekta ekta kore item minus kore append kora better
