def plusone(digits):
    n = len(digits)
    if digits[-1] == 9:
        if n == 1:
            return [1, 0]
        return digits[:-1] + [0]
    else:
        digits[-1] += 1
    return digits


print(plusone([1, 2, 9]))
