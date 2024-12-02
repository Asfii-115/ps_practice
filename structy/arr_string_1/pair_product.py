def p_and_s(numbers, target):
    previous_numbers = {}
    for index, num in enumerate(numbers):
        compliment = target / num
        if compliment in previous_numbers:
            return (previous_numbers[compliment], index)
        previous_numbers[num] = index