def even_numbers(arr,n):
    arr_r = arr[::-1]
    li = []
    x = 0
    while len(li)!=n:
        if arr_r[x]%2==0:
            li.append(arr_r[x])
        x+=1
    return li[::-1]        


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))        