# def filter_list(l):
#     return [x for x in l if not isinstance(x, str)]


# print(filter_list([1, 2, "a", "b"]))


# import math


# def is_square(n):
#     return n > -1 and math.sqrt(n) % 1 == 0


# print(is_square(25))


# def accum(st):
#     s = ""
#     x = 0
#     i = 0
#     while len(st) != 0:
#         s += st[x]
#         x += 1
#         i -= 1
#     return s


# print(accum("abcd"))


def solution(nums):
    if nums:
        nums.sort()
        return nums
    else:
        return []


print(solution(None))


def capitals(word):
    # your code here
    li = []
    for x in range(len(word)):
        if word[x].isupper():
            li.append(x)
    return li


print(capitals("CodEWaRs"))


def small_enough(array, limit):
    return max(array) <= limit


print(small_enough([66, 100], 200))
