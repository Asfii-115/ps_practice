def sumarray(arr):
    result = []
    result.insert(0, arr[0])
    for x in range(1, len(arr)):
        arr[x] = arr[x - 1] + arr[x]
        result.append(arr[x])
    return result


print(sumarray([3, 1, 2, 10, 1]))
