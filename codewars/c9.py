# def get_middle(s):
#     n = len(s)
#     if n % 2 == 1:
#         return s[(n // 2)]
#     else:
#         return s[(n // 2) - 1 : (n // 2) + 1]


# print(get_middle("testingg"))


# def descending_order(num):
#     str1 = str(num)
#     li = []
#     for x in range(len(str1)):
#         li.append(str1[x])
#     li.sort(reverse=True)
#     return "".join(map(int, li))


# # print(descending_order(56981))
# def xo(s):
#     # if "x" or "X" or "o" or "O" not in s:
#     #     return True
#     x_count = 0
#     o_count = 0
#     for i in s:
#         if i == "x" or i == "X":
#             x_count += 1
#         if i == "o" or i == "O":
#             o_count += 1

#     return x_count == o_count


# print(xo("zpzppp"))
# print(xo("ooxxx"))
# print(xo("xooxxxx"))


# def xo(s):
#     s = s.lower()
#     return s.count("x") == s.count("o")
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])


# print(sum_two_smallest_numbers([1, 2, 3, 4, 5, 6]))


def get_sum(a, b):
    sum = 0
    if a > 0 and b == 0:
        return a + b
    for x in range(a, b + 1):
        sum += x
    return sum


print(get_sum(-1, 2))
