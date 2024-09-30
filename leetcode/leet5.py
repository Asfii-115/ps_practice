# def fdiff(s, t):
#     y = ""
#     z = ""
#     for x in range(len(t) - 1):
#         if t[x] in s:
#             y += s[x]
#         else:
#             z += s[x]

#     return y, z


# print(fdiff("abcd", "abcde"))


def diff(s, t):
    i = 0
    while i < len(s):
        if s[i] != t[i]:
            return t[i]
        i += 1
    return t[i]


print(diff("abcd", "ambcd"))
