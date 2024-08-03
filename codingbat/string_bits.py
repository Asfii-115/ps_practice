# def string_bits(str):
#     x = 0
#     res = ""
#     i = 0
#     for i in range(len(str)):
#         res = res + str[(0 + x)]
#         x += 2
#         i += 1
#         return res


# print(string_bits("asfi"))


def string_bits(str):
    result = ""
    # Many ways to do this. This uses the standard loop of i on every char,
    # and inside the loop skips the odd index values.
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


print(string_bits("asfi"))
