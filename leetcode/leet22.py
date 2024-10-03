def countodd(low, high):
    count = 0
    for x in range(low, high + 1):
        if x % 2 == 1:
            count += 1
    return count


print(countodd(8, 10))
