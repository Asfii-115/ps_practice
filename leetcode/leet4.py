class Solution:
    def findTheDifference(s: str, t: str) -> str:
        for x in t:
            if x in s:
                s = s.replace(x, "")
            else:
                return x

    print(findTheDifference("avsy", "tavsy"))
