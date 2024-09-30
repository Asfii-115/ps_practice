class Solution:
    def strStr(haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle[0:])
        else:
            return -1

    print(strStr("mississippi", "issip"))
