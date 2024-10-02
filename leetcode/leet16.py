def ar_prog(arr):
    if len(arr) <= 1:
        return False

    s_arr = sorted(arr)

    diff = s_arr[1] - s_arr[0]

    for x in range(1, len(s_arr)):
        if s_arr[x] - s_arr[x - 1] != diff:
            return False
    return True


print(ar_prog([1, 2, 4]))
