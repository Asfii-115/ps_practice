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


def sq(n):
    i = 1
    while i < n:
        if n / i == i:
            return (i + 1) ** 2
        else:
            i += 1


print(sq(121))
