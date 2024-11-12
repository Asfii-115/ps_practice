def flatten_and_sort(array):
    lst = []
    for x in array:
        for y in x:
            lst.append(y)
    return sorted(lst)

print(flatten_and_sort([[], [], []]))        
