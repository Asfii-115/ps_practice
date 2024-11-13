def find_uniq(arr):
    ul = []
    for x in arr:
        if x not in ul:
            ul.append(x)
    return ul[-1]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))  

def fu(arr):
    s = set(arr)
    for x in s:
        if arr.count(x)==1:
            return x
        

def tower_builder(n_floors):
    li = []
    for x in range(n_floors):
        for y in range(1,n_floors,2):
            li.append('*')
    return li

print(tower_builder(3))        
