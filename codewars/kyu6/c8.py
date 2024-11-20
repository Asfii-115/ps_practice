def find_even_index(arr):
    n = (len(arr)//2)+1
    return sum(arr[:n]) == sum(arr[n:])

print(find_even_index([1,2,3,4,3,2,1]))