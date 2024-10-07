def codds(low, high):
    if low % 2 != 0:
        return len(range(low, high + 1, 2))
    return len(range(low + 1, high, 2))


print(codds(8, 10))
