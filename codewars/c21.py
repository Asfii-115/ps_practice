def row_weights(array):
    a = 0
    b = 0
    lst = []
    for x in range(0,len(array),2):
        a+= array[x]
    for x in range(1,len(array),2):
        b+= array[x]
    lst.append(a)    
    lst.append(b)    
    return tuple(lst)
       


print(row_weights([13,27,49]))

def rw(arr):
    return [sum(arr[::2]),sum(arr[1::2])]
print(rw([13,27,49]))