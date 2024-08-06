def close_far(a, b, c):
    if (
        abs(a) - abs(b) <= 1
        and (abs(c) >= abs(a) + 2 or abs(c) + 2 <= abs(a))
        and (abs(c) >= abs(b) + 2 or abs(c) + 2 <= abs(b))
    ):
        return True
    elif (
        abs(a) - abs(c) <= 1
        and (abs(b) >= abs(a) + 2 or abs(b) + 2 <= abs(a))
        and (abs(b) >= abs(c) + 2 or abs(b) + 2 <= abs(c))
    ):
        return True
    return False
    # elif abs(a) - abs(c) <= 1 and abs(b) >= abs(a) + 2 and abs(b) >= abs(c) + 2:
    #     return True
    # elif (abs(a) - abs(c) <= 1) and (abs(a) - abs(b) >= 2 and abs(c) - abs(b) >= 2):
    #     return True


print(close_far(1, 2, 3))


def close_far(a, b, c):
    def is_close(x, y):
        return abs(x - y) <= 1

    def is_far(x, y):
        return abs(x - y) >= 2

    if is_close(a, b) and is_far(a, c) and is_far(b, c):
        return True
    if is_close(a, c) and is_far(a, b) and is_far(c, b):
        return True

    return False


# Test cases
print(close_far(1, 2, 10))  # Should return True
print(close_far(1, 2, 3))  # Should return False
print(close_far(4, 1, 3))  # Should return True
print(close_far(1, 1, 2))  # Should return False
print(close_far(3, 5, 1))  # Should return True
