def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))


print(merge_arrays([1, 2, 3, 4, 5, 5], [6, 7, 8, 9, 10]))