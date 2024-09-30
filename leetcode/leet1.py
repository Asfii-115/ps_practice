# def lengthOfLastWord(s: str) -> int:
#     return len(s)


# print(lengthOfLastWord("Hello World"))


# class Solution:
#     def longestCommonPrefix(strs: list[str]) -> str:
#         ans = ""
#         strs = sorted(strs)
#         first = strs[0]
#         last = strs[-1]
#         for x in range(min(len(first), len(last))):
#             if first[x] != last[x]:
#                 return ans
#             ans += first[x]
#         return ans

#     print(longestCommonPrefix(["flower", "flow", "flight"]))
