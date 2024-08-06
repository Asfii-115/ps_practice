def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    mod = num % 10
    if mod == 0:
        return num
    elif mod >= 5:
        return num + (10 - mod)
    else:
        return num - mod


print(round_sum(6, 4, 4))
