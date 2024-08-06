def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    elif n >= 13 and n <= 19:
        return 0
    else:
        return n


print(no_teen_sum(2, 1, 15))

# gpt
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n


# Test cases
print(no_teen_sum(1, 2, 3))  # Should return 6
print(no_teen_sum(2, 13, 1))  # Should return
