import re


def pali(s):
    s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
    return s == s[::-1]


print(pali("A man, a plan, a canal: Panama"))


def twosum(l, t):
    for x in range(len(l) - 1):
        if l[x] + l[x + 1] == t:
            return [x, x + 1]


print(twosum([2, 11, 15, 7], 9))
