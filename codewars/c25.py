def get_even_numbers(arr):
    return list(filter(lambda y:y%2==0, arr))

print(get_even_numbers([2,4,5,6]))