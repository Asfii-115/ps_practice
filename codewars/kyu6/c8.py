def find_even_index(arr):
    if not arr:
        return arr
    if len(arr) == 1:
        return 0
    i = 0
    while i < len(arr):
        if sum(arr[:i]) == sum(arr[i + 1 :]):
            return i
        else:
            i += 1


print(find_even_index([7, 3, -3]))
