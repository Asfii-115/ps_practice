# def iso(s):
#     s = s.lower()
#     for x in range(len(s)):
#         v = s.count(s[x])
#         if v > 1:
#             return False
#     return True


# print(iso("aba"))


# def longest(a, b):
#     x = a + b
#     x = set(x)
#     return "".join(sorted(x))


# print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))


# def sq(n):
#     i = 1
#     while i < n:
#         if n / i == i:
#             return (i + 1) ** 2
#         else:
#             i += 1


# print(sq(121))


# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i, "")
#     return s


# def find_short(s):
# s = s.split()
#     min = len(s[0])
#     for x in range(len(s)):
#         if len(s[x]) < min:
#             min = len(s[x])
#     return min


# print(find_short("lets to about javascript the best language"))


# def find_short(s):
#     return min(len(x) for x in s.split())


def open_or_senior(data):
    # for x in data:
    #     if x[0] >= 55 and (x[1] >= -2 and x[1] <= 26):
    #         return "senior"
    #     else:
    #         return "open"
    return ["open" for x in data if x[0] >= 55 and (x[1] >= -2 and x[1] <= 26)]


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
