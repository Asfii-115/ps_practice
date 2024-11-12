def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])

print(largest_pair_sum([10, 14, 2, 23, 19]))