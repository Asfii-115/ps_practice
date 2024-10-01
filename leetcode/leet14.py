# def fdiff(s, t):
#     x = 0
#     while x < len(s):
#         if s[x] != t[x]:
#             return t[x]
#         x += 1
#     return t[x]


def fdiff(s, t):
    sum_s = 0
    sum_t = 0
    for x in range(len(s)):
        sum_s += ord(s[x])
        sum_t += ord(t[x])
    sum_t += ord(t[-1])

    return chr(sum_t - sum_s)


print(fdiff("abcd", "abcde"))
