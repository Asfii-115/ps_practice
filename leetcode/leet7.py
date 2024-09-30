# def anagram(s, t):
#     s2 = ""
#     if len(s)
#     for x in s:
#         if x in t:
#             s2 += x

#     return len(s2) == len(t)


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s2 = ""

#         for x in s:
#             if x in t:
#                 s2 += x

#         return len(s2) == len(t)


def anagram(s, t):
    return sorted(s) == sorted(t)


print(anagram("ccaa", "ccac"))
