def max_diff(lst):
    max_value = lst[0]
    min_value = lst[0]

    for num in lst[1:]:
        if num>max_value:
            max_value = num

    for num in lst[1:]:
        if num<min_value:
            min_value = num   
    
    return max_value - min_value

print(max_diff([0, 1, 2, 3, 4, 5, 6]))             
