def pair_sum(numbers, target_sum):
    for x in range(len(numbers)):
        for y in range(1, len(numbers)):
            if numbers[x] + numbers[y] == target_sum:
                return (x, y)


def pair_sum_again(numbers, t):
    hash_map = {value: index for index, value in enumerate(numbers)}
    for x in range(len(numbers)):
        if t - numbers[x] in hash_map:
            return (x,)


print(pair_sum_again([3, 2, 5, 7, 9], 8))


def p_and_s(numbers, target):
    previous_numbers = {}
    for index, num in enumerate(numbers):
        compliment = target - num
        if compliment in previous_numbers:
            return (previous_numbers[compliment], index)
        previous_numbers[num] = index


print(p_and_s([3, 2, 5, 4, 1], 8))
