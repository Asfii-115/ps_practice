# def abbrev_name(name):
#     first, last = name.upper().split()
#     return first[0] + "." + last[0]


def abbrev_name(name):
    return ".".join(x[0] for x in name.upper().split())


print(abbrev_name("Sam Harris"))


# def century(year):
#     # n = year % 100
#     # if n >= 1:
#     #     return (year // 100) + 1
#     # return year // 100
#     return (year // 100) + 1 if (year % 100) >= 1 else year // 100


# def century(year):
#     return (year + 99) // 100

# import math


# def century(year):
#     return math.floor(year / 100)
#     return math.ceil(year / 100)


# print(century(2701))


# def digitize(n):

#     return [int(x) for x in str(n)][::-1]


# def digitize(n):
#     return list(map(int, str(n)[::-1]))


# print(digitize(34567))


# def count_positives_sum_negatives(arr):
#     # count = 0
#     # for x in range(len(arr)):
#     #     if arr[x] >= 1:
#     #         count += 1
#     return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]


# def count_positives_sum_negatives(arr):
#     if not arr:
#         return [0, 0]
#     elif len(arr) <= 2 and (arr[0] == 0 and arr[1] == 0):
#         return []
#     else:
#         return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]


# print(
#     count_positives_sum_negatives(
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
#     )
# )


# def fake_bin(x):
#     li = list(map(int, str(x)))
#     for i in range(len(li)):
#         if li[i] < 5:
#             li[i] = 0
#         else:
#             li[i] = 1
#     return "".join(map(str, li))


# print(fake_bin(3456))


def smash(words):
    i = ""
    for x in words:
        i = i + " " + x
    return i.strip()


print(smash(["hello", "world", "this", "is", "great"]))
