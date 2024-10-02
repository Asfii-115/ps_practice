def add_one(arr):
    if arr[-1] != 9:
        arr[-1] += 1
    else:
        arr[-1] = 0
        arr.insert(arr[-1] + 1)
    return arr


print(add_one([9]))
